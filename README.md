# AI Presentation Generator

An AI-powered presentation generator that creates professional PowerPoint presentations using Groq AI.

## Features

- 🎯 Generate complete presentations from a topic
- 🎨 Professional slide layouts
- 📊 Customizable number of slides and points
- 💫 Easy-to-use web interface
- 🔄 Real-time generation

## Installation

1. Clone the repository:

    bash
    git clone https://github.com/rushisur/ai-presentation-generator.git
    cd ai-presentation-generator


2. Install dependencies:
    bash
    pip install -r requirements.txt

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your Groq API key to `.env`

## Usage

1. Run the Streamlit app:
    bash
    streamlit run app.py

2. Open your browser and go to `http://localhost:8501`

3. Enter your Groq API key in the sidebar

4. Input your presentation topic and customize settings

5. Click "Generate Presentation" and download the result

## Requirements

- Python 3.7+
- Groq API key (get it from [console.groq.com](https://console.groq.com))
- Required Python packages (see requirements.txt)

## Configuration

The application can be configured using the following environment variables:
- `GROQ_API_KEY`: Your Groq API key

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security

⚠️ Never commit your API keys or sensitive information to the repository.
Always use environment variables for sensitive data.