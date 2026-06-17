import os 
from pathlib import Path
from dotenv import load_dotenv  
from google import genai

# Resolve the absolute path to the .env file
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

class GeminiClient:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        
        # Clean the API key in case it's loaded as empty string or whitespace
        if api_key:
            api_key = api_key.strip()
            
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing or empty in your environment or .env file.\n"
                "Please open your .env file at backend/.env and set GEMINI_API_KEY to a valid Gemini API key."
            )
            
        print("API KEY FOUND: True")
        self.client = genai.Client(api_key=api_key)
        # Try GEMINI_MODEL first, fallback to LLM_MODEL, default to gemini-1.5-flash
        self.model_name = (os.getenv("GEMINI_MODEL") or os.getenv("LLM_MODEL") or "gemini-1.5-flash").strip()

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        return response.text

        