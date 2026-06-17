import chromadb
from app.models.chunk import Chunk


class VectorStore:
    def __init__(
        self,
        db_path: str = "./chroma_db",
        collection_name: str = "cloudflow_docs",
    ):

        self.db_path = db_path
        self.collection_name = collection_name
        self.client = chromadb.PersistentClient(
            path=self.db_path
        )

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

    def reset_collection(self):
        try:
            self.client.delete_collection(
                name=self.collection_name
            )
            print(f"Deleted collection: {self.collection_name}")
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )
        print(f"Created collection: {self.collection_name}")

    def add_chunks(
        self,
        chunks: list[Chunk],
        embeddings,
    ):
        ids = []
        documents = []
        metadatas = []
        vectors = []

        for chunk, embedding in zip(chunks, embeddings):

            ids.append(chunk.chunk_id)

            documents.append(chunk.text)

            vectors.append(
                embedding.tolist()
            )

            metadatas.append(
                {
                    "document_id": chunk.document_id,
                    "document_name": chunk.document_name,
                    "category": chunk.category,
                }
            )

        self.collection.upsert(
            ids=ids,
            embeddings=vectors,
            documents=documents,
            metadatas=metadatas,
        )

        print(
            f"Stored {len(ids)} chunks in ChromaDB"
        )

    def count(self):
        return self.collection.count()