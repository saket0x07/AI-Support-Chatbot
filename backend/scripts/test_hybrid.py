from app.rag.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

result = retriever.search("refund policy")

for i,doc in enumerate(result, start=1):
    print(f"\nResult {i}")
    print(doc[:300])
    