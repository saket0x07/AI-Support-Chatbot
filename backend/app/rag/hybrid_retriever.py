from transformers.models.deformable_detr import image_processing_deformable_detr_fast
from transformers.models.deformable_detr import image_processing_deformable_detr_fast
from app.rag.retriver import Retriver
from app.rag.bm25_retriever import BM25Retriver

class HybridRetriever:
    
    def __init__(self):
        self.vector_retriever = Retriver()
        all_docs = self.vector_retriever.vector_store.collection.get()
        self.bm25 = BM25Retriver(all_docs["documents"])
        self.doc_to_meta = {}
        if all_docs and "documents" in all_docs and "metadatas" in all_docs:
            docs = all_docs["documents"] or []
            metas = all_docs["metadatas"] or []
            for doc, meta in zip(docs, metas):
                if doc:
                    self.doc_to_meta[doc] = meta if meta is not None else {}
    
    def search(self,query,top_k=5,w1=0.6,w2=0.4):
        vector_results = self.vector_retriever.search(query=query,top_k=top_k)
        vector_docs = vector_results["documents"][0]

        bm25_docs= self.bm25.search(query=query,top_k=top_k)
        
        merged = [] 
        
        for doc in vector_docs+bm25_docs:
            if doc not in merged:
                merged.append(doc)    
        return merged[:top_k]
    