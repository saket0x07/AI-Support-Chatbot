import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.utils.loaders import load_documents
from app.rag.chunker import chunk_documents
docs = load_documents()
chunks = chunk_documents(docs,chunk_size=500,chunk_overlap=50)

print(f"loaded {len(docs)} documents")
print(f"chunked into {len(chunks)} chunks")

print("\n First chunk ")
print(chunks[0].text[:300])


