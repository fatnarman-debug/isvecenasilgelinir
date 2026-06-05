import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
try:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    client.models.generate_content(model="gemini-3.5-flash", contents="Hello")
    print("Success")
except Exception as e:
    print(f"Error: {e}")
