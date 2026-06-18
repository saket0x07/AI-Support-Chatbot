import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.rag.embedder import Embedder
import shutil

from app.utils.loaders import load_documents
from app.rag.chunker import chunk_documents
# from app.rag.embedder import embed_chunks
from app.rag.vector_store import VectorStore

def main():
    chroma_path=Path("db/chroma_db")
    if chroma_path.exists():
        shutil.rmtree(chroma_path)
        print("Cleared old ChromaDB")
    print("Loading documents....")
    docs = load_documents()
    print(f"\n loaded{len(docs)}documents")
    print("\n Chunking documents...\n")
    chunks=chunk_documents(docs,chunk_size=1000,chunk_overlap=100)
    print(f"\n Created {len(chunks)} chunks\n")

    print("\n Embedding documents...\n")
    embedder = Embedder()
    embeddings = embedder.embed_chunks(chunks)
    print("\nSaving to ChromaDB...\n")
    vector_store=VectorStore()
    vector_store.add_chunks(chunks,embeddings)

    print("\n All done! knowledge base updated.\n")

if __name__ == "__main__":
    main()