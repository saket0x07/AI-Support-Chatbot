from dataclasses import dataclass

@dataclass
class Chunk:
    chunk_id: str
    document_id: str
    document_name: str
    category: str
    text: str
