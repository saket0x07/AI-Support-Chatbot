from pathlib import Path
from typing import List
from app.models.document import Document

def load_documents() -> List[Document]:
    """ load all markdown files from backend/data/raw_docs """
    project_root = Path(__file__).resolve().parents[2]
    docs_path = project_root / "data" / "raw_docs"
    documents = []

    for filepath in docs_path.rglob("*.md"):
        try:
            documents.append(
                Document(
                    id=str(filepath.stem),
                    filename=filepath.name,
                    filepath=str(filepath),
                    category=filepath.parent.name,
                    content=filepath.read_text(encoding="utf-8")
                )
            )
        except Exception as e:
            print(f"error loading {filepath}:{e}")
    
    return documents
