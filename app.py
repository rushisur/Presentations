import streamlit as st
import os
from slides_generator import generate_presentation
import base64
import tempfile
from groq import Groq 
from io import BytesIO  # Import Groq client directly

# Configure Streamlit page
st.set_page_config(
    page_title="AI Presentation Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Replace the existing get_download_link function with this:
def get_download_link(presentation, filename):
    """Generate a download link for the presentation"""
    try:
        # Use in-memory bytes buffer instead of temporary files
        buffer = BytesIO()
        presentation.save(buffer)
        buffer.seek(0)  # Rewind the buffer
        bytes_data = buffer.getvalue()
        buffer.close()  # Explicitly close the buffer

        b64 = base64.b64encode(bytes_data).decode()
        return f'<a href="data:application/vnd.openxmlformats-officedocument.presentationml.presentation;base64,{b64}" download="{filename}">Download Presentation</a>'
    
    except Exception as e:
        st.error(f"Error creating download link: {str(e)}")
        raise

def main():
    st.title("🎯 AI Presentation Generator")
    st.write("Generate professional presentations using AI")

    # Sidebar for API key
    with st.sidebar:
        st.header("Configuration")
        api_key = st.text_input("Enter Groq API Key", type="password", key="api_key")
    
    # Main content area
    topic = st.text_input(
        "Enter your presentation topic:",
        placeholder="e.g., Artificial Intelligence and Its Impact on Society"
    )

    col1, col2 = st.columns(2)
    with col1:
        num_slides = st.slider("Number of slides", min_value=3, max_value=10, value=4)
    with col2:
        points_per_slide = st.slider("Points per slide", min_value=2, max_value=6, value=3)

    if st.button("Generate Presentation", type="primary"):
        if not api_key:
            st.error("Please enter your Groq API key in the sidebar!")
            return

        if not topic:
            st.error("Please enter a presentation topic!")
            return

        try:
            with st.spinner("🎨 Generating your presentation..."):
                # Initialize Groq client directly
                client = Groq(api_key=api_key)
                
                # Generate presentation
                prs = generate_presentation(
                    client=client,  # Pass the properly initialized client
                    topic=topic,
                    num_slides=num_slides,
                    points_per_slide=points_per_slide
                )
                
                # Create filename
                output_file = f"{topic.replace(' ', '_').lower()}.pptx"
                
                # Create download link
                download_link = get_download_link(prs, output_file)
                
                # Show success message and download button
                st.success("✨ Presentation generated successfully!")
                st.markdown(download_link, unsafe_allow_html=True)
                
                # Preview information
                with st.expander("📑 Presentation Details", expanded=True):
                    st.write(f"**Topic:** {topic}")
                    st.write(f"**Filename:** {output_file}")
                    st.write(f"**Number of slides:** {num_slides}")
                    st.write(f"**Points per slide:** {points_per_slide}")
                
        except Exception as e:
            st.error(f"Error generating presentation: {str(e)}")
            if "authentication" in str(e).lower():
                st.warning("Please check if your Groq API key is valid!")

if __name__ == "__main__":
    main()