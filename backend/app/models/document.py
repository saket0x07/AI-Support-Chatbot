from dataclasses import dataclass

@dataclass
class Document:
    id: str
    filename: str
    filepath: str
    category: str
    content: str