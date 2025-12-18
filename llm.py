import google.generativeai as genai 
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def ask_llm(prompt):
    response = model.generate_content(prompt)
    return response.text