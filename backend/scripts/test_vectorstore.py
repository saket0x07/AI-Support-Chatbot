from app.utils.loaders import load_documents
from app.rag.chunker import chunk_documents
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore


documents = load_documents()

chunks = chunk_documents(
    documents,
    chunk_size=500,
    chunk_overlap=50
)

embedder = Embedder()

embeddings = embedder.embed_chunks(
    chunks
)

vector_store = VectorStore()

vector_store.add_chunks(
    chunks,
    embeddings,
)

print(
    f"Total vectors: {vector_store.count()}"
)