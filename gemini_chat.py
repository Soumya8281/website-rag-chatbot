import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(context, question):

    prompt = f"""
    You are a helpful AI assistant.

    Use the following website content to answer the question.

    Website Content:
    {context}

    Question:
    {question}

    Answer:
    """

    response = model.generate_content(prompt)

    return response.text