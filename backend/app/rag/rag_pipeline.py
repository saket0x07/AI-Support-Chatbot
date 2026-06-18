from app.rag.hybrid_retriever import HybridRetriever
from app.rag.reranker import Reranker
from app.rag.prompt import PromptBuilder

from app.llm.gemini_client import GeminiClient
from app.nlp.query_processor import QueryProcessor


class RAGPipeline:

    def __init__(self):

        self.retriever = HybridRetriever()
        self.reranker = Reranker()

        self.llm = GeminiClient()
        self.query_processor = QueryProcessor()

    def answer(
        self,
        query: str,
        history=None
    ) -> dict:


        # NLP ANALYSIS
        query_info = self.query_processor.process(query)

        print("\n===== QUERY ANALYSIS =====")
        print(query_info)

        # HYBRID RETRIEVAL       

        retrieval_results = self.retriever.search(
            query=query,
            top_k=20
        )
        docs = retrieval_results
        print(f"\nRetrieved {len(docs)} documents")

        # RE-RANKING
        reranked_docs = self.reranker.rerank(
            query=query,
            docs=docs,
            top_k=5
        )

        print(f"Re-ranked to {len(reranked_docs)} documents")


          #Retriend Docs

        print("===========RETRIEVED DOCS==================")
        for i,doc in enumerate(reranked_docs,start=1):
            print(f"\n --DOC{i}--\n")
            print(doc[:1500])

        # PROMPT BUILDING

        reranked_metas = [
            self.retriever.doc_to_meta.get(doc, {"document_name": "Unknown"})
            for doc in reranked_docs
        ]

        results = {
            "documents": [reranked_docs],
            "metadatas": [reranked_metas]
        }

        prompt = PromptBuilder.build_prompt(
            query=query,
            results=results,
            history=history
        )

        # LLM GENERATION
        response = self.llm.generate(prompt)

        # Extract unique sources
        sources = []
        for meta in reranked_metas:
            source_name = meta.get("document_name")
            if source_name and source_name not in sources:
                sources.append(source_name)
        # FINAL OUTPUT

        return {
            "query_analysis": query_info,
            "retrieved_docs": reranked_docs,
            "answer": response,
            "sources": sources
        }