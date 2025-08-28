import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Streamlit page
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

# App title and description
st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

# Get the Google API key and configure the generative AI library
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# User inputs
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targetting (optional)")

# Analyze button
analyze = st.button("Analyze Resume")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file) 
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to extract text from an uploaded file
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")
    
# Logic for when the button is pressed
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()
        
        # Build the prompt for the LLM
        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job application'}

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations."""

        # Call the Gemini API
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        # Display the analysis results
        st.markdown("### Analysis Results")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")