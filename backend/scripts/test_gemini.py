from app.llm.gemini_client import GeminiClient

c = GeminiClient()

response = c.generate("Explain ml in one sentence")
print(response)