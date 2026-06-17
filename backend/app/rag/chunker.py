from app.models.document import Document
from app.models.chunk import Chunk

def chunk_documents(
    documents: list[Document],
    chunk_size: int = 500,
    chunk_overlap: int = 50
) -> list[Chunk]:
    """
    Chunks a list of Document objects into Chunk dataclasses without external dependencies.
    """
    chunks: list[Chunk] = []

    for document in documents:
        content = document.content.strip()
        if not content:
            continue

        start = 0
        idx = 0
        while start < len(content):
            end = start + chunk_size
            chunk_text = content[start:end]
            chunks.append(
                Chunk(
                    chunk_id=f"{document.id}-chunk-{idx}",
                    document_id=document.id,
                    document_name=document.filename,
                    category=document.category,
                    text=chunk_text
                )
            )
            start += chunk_size - chunk_overlap   
            idx += 1

    return chunks   