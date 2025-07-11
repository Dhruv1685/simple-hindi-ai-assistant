import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env and configure
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

# Use correct model and method
model = genai.GenerativeModel("gemini-1.5-flash")
  # ⚠️ "models/" prefix is important

def ask_gpt(hindi_text):
    base_path = os.path.dirname(os.path.abspath(__file__))
    command_file = os.path.join(base_path, "command_list.txt")

    if not os.path.exists(command_file):
        return "⚠️ 'command_list.txt' file nahi mila. Kripya project folder mein daaliye."

    with open(command_file, "r", encoding="utf-8") as f:
        examples = f.read()

    prompt = f"""
Yeh ek Hindi voice assistant hai. User ne yeh Hindi command diya: "{hindi_text}"

Niche kuch example diye gaye hain Hindi command aur unke Python code ke:
{examples}

Ab user ke command ke liye bhi ek Python code likho.

Reply sirf iss format mein hona chahiye:

Action: (Hindi mein batayein kya hoga)
Code: (Python code)
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini error: {str(e)}"
