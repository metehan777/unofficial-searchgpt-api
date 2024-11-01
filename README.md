# Alternative SearchGPT API

This project provides a RESTful API that integrates web search capabilities with OpenAI's GPT-4o model to deliver concise, AI-generated responses based on real-time web information.

## Features
- **GET and POST Endpoints**: Handle user queries via both GET and POST HTTP methods.
- **Web Search Integration**: Fetches relevant web snippets using Bing's Web Search API.
- **AI-Generated Responses**: Utilizes OpenAI's GPT-4o model to generate informative answers.

## Prerequisites
- Python 3.x
- API keys for OpenAI and Bing Search API

## Installation

### Clone the Repository:

    git clone https://github.com/metehan777/unofficial-searchgpt-api.git
    cd unofficial-searchgpt-api

# Install Dependencies

    pip install -r requirements.txt

# Set Environment Variables

    export OPENAI_API_KEY='your_openai_api_key'
    export BING_API_KEY='your_bing_api_key'

# Run the Application

    python app.py

# The API will be accessible at `http://127.0.0.1:5000/`

# Send a GET Request

    curl "http://127.0.0.1:5000/api/search?query=What is the capital of France?"

# Send a POST Request

    curl -X POST "http://127.0.0.1:5000/api/search" -H "Content-Type: application/json" -d '{"query": "What is the capital of France?"}'

# Example JSON Response Format

    # {
    #   "query": "What is the capital of France?",
    #   "answer": "The capital of France is Paris.",
    #   "sources": [
    #     "Source 1: Paris is the capital city of France.",
    #     "Source 2: The capital of France is Paris, known for its art, fashion, and culture."
    #   ]
    # }


# Notes
- Ensure your OpenAI and Bing API keys are valid and have the necessary permissions.
- For more advanced features, consider implementing additional functionalities such as error handling, logging, and authentication.

# License
- *This project is not licensed.

# Acknowledgments
- OpenAI for the GPT-4o model.
- Bing Search API for web search capabilities.
- By following these steps, you can set up and run an alternative to SearchGPT, capable of handling both GET and POST requests to process user queries and generate AI-driven responses based on real-time web information.


