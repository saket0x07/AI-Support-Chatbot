from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore

class Retriver:

    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()   
    
    def search(self,query:str,top_k:int=5):
        query_embedding = self.embedder.embed_text(query)
        results = self.vector_store.collection.query(query_embeddings = [query_embedding.tolist()],
        n_results=top_k,

        )
   
        return results
        