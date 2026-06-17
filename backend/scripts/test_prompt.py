from app.rag.retriver import Retriver
from app.rag.prompt import PromptBuilder

retriver = Retriver()
results = retriver.search(query="How do i cancel my subscription?")

prompt = PromptBuilder.build_prompt(query="How do i cancel my subscription?",results=results)
print(prompt)