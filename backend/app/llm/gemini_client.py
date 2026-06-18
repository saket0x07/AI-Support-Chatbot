import os 
from pathlib import Path
from dotenv import load_dotenv  

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
        
        # Determine if we are using OpenRouter or standard Gemini API
        self.is_openrouter = api_key.startswith("sk-or-")
        
        # Try GEMINI_MODEL first, fallback to LLM_MODEL, default to gemini-2.5-flash
        model = (os.getenv("GEMINI_MODEL") or os.getenv("LLM_MODEL") or "gemini-2.5-flash").strip()
        
        if self.is_openrouter:
            from openai import OpenAI
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key
            )
            # Adapt model name for OpenRouter if needed
            if "/" not in model:
                if model.startswith("gemini-"):
                    model = f"google/{model}"
            self.model_name = model
            print(f"Using OpenRouter with model: {self.model_name}")
        else:
            from google import genai
            self.client = genai.Client(api_key=api_key)
            self.model_name = model
            print(f"Using standard Gemini API with model: {self.model_name}")

    def generate(self, prompt: str) -> str:
        if self.is_openrouter:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000,
            )
            return response.choices[0].message.content
        else:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            return response.text

        