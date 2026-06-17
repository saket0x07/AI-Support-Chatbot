from app.rag.retriver import Retriver

retriver = Retriver()

query = "How do i cancel my subscription?"
results = retriver.search(query=query,top_k=3)

print("\nQuery:")
print(query)

print("\nResults")

for i, doc in enumerate(results["documents"][0],start=1):
   
    print("\n" + "-"*60)
    print(f"Result {i}")
    print("-" * 60)

    print(doc[:1000])