from app.utils.loaders import load_documents
from app.rag.chunker import chunk_documents
from app.rag.embedder import Embedder

documents = load_documents()
chunks = chunk_documents(documents,chunk_size=500,chunk_overlap=50)

print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")

embedder = Embedder()
embeddings = embedder.embed_chunks(chunks)
print(f"Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {embedder.embedding_dimension()}")

print("\n First vector shape :")
print(embeddings[0].shape)

print("\n First vector :")
print(embeddings[0].shape)
