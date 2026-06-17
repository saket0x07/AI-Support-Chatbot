import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.utils.loaders import load_documents
docs = load_documents()

print(f"loaded {len(docs)} documents")
for doc in docs[:3]:
    print(doc.filename)
    print(doc.category)
