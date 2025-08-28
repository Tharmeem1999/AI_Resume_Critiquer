# AI Resume Critiquer

## Overview
This project is an AI-powered web application built with Streamlit that allows users to upload their resume (in PDF or TXT format) and receive tailored feedback from Google's Gemini model. The application analyzes the resume for content clarity, skills presentation, experience descriptions, and provides specific improvement suggestions, optionally tailored to a target job role. This project demonstrates the integration of a large language model (LLM) with a user-friendly web interface, file processing, and API key management, making it a great example of combining AI with practical applications.

## Project Steps
Here’s a step-by-step guide to setting up and running the project:

1. **Initialize a New UV Project**  
   Inside your project directory, initialize a new UV project to set up a virtual environment and project structure:  
   ```bash
   uv init .
   ```

2. **Install Dependencies**  
   Install the required Python packages using UV, a faster alternative to pip for package installation and dependency resolution:  
   ```bash
   uv add google-generativeai streamlit PyPDF2 python-dotenv
   ```

3. **Create an Environment File**  
   Create a `.env` file in the project root to store environment variables, such as the API key for the LLM provider:  
   ```bash
   touch .env
   ```  
   Add your API key to the `.env` file in the format:  
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```  
   Replace `your_api_key_here` with the actual API key.

4. **Obtain an API Key**  
   This project uses the Google Gemini API, but you can use an API key from any compatible LLM provider (e.g., OpenAI, Anthropic, etc.). To get a Google Gemini API key:  
   - Visit the Google Cloud Console or the Gemini API provider’s website.  
   - Create a new project and enable the Gemini API.  
   - Generate an API key and copy it to the `.env` file.

5. **Write the Code**  
   Create a `main.py` file and implement the code for the AI Resume Critiquer. The code:  
   - Uses Streamlit to create a web interface for file upload and user input.  
   - Extracts text from uploaded PDF or TXT files using PyPDF2 or direct decoding.  
   - Constructs a prompt for the Gemini model to analyze the resume and provide structured feedback.  
   - Displays the AI-generated feedback in a clear, formatted manner.  
   See the `main.py` file in this repository for the complete implementation.

6. **Run the Application**  
   Activate the UV virtual environment and run the Streamlit app:  
   ```bash
   uv run streamlit run main.py
   ```  
   Open the provided local URL (typically `http://localhost:8501`) in a browser to interact with the app. Upload a resume, optionally specify a job role, and click "Analyze Resume" to view the feedback.

## Python Packages Used
The following Python packages are required for this project:
- **google-generativeai**: Provides access to Google’s Gemini models for generating resume feedback.
- **streamlit**: A Python library for creating interactive web applications with minimal code.
- **PyPDF2**: Enables extraction of text from PDF files for resume processing.
- **python-dotenv**: Loads environment variables from a `.env` file for secure API key management.
- **uv**: A high-performance Python package installer and resolver used instead of pip for dependency management.

## Additional Information
- **How to Use the Application**:  
   After running the app, access it via a web browser. Upload a resume (PDF or TXT), optionally enter a target job role, and click "Analyze Resume." The app will display AI-generated feedback focusing on content clarity, skills presentation, experience descriptions, and tailored improvements.

- **Why UV?**  
   UV is a modern, high-performance alternative to pip, offering faster dependency resolution and installation. It simplifies project setup and ensures a clean virtual environment. Learn more at [UV’s official documentation](https://docs.astral.sh/uv/).
