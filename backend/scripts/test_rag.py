from app.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()


query = "How do i cancel my Subscription?"
response = rag.answer(query)

print("\n Query: ")
print(query)
print("\n RAG Response: ")
print(response) 
print("\n ANSWER: ")
print(response['answer']) 
print("\n ANALYSIS: ")
print(response['query_analysis']) 


