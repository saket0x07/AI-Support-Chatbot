from sentence_transformers import SentenceTransformer
from app.models.chunk import Chunk


class Embedder:

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):
        return self.model.encode(
            text,
            convert_to_numpy=True
        )

    def embed_chunks(self, chunks: list[Chunk]):
        texts = [chunk.text for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True,
        )

        return embeddings

    def embedding_dimension(self) -> int:
        sample = self.embed_text("hello world")
        return len(sample)