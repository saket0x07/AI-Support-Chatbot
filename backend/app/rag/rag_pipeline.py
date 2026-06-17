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

        # ==========================
        # NLP ANALYSIS
        # ==========================

        query_info = self.query_processor.process(query)

        print("\n===== QUERY ANALYSIS =====")
        print(query_info)

        # ==========================
        # HYBRID RETRIEVAL
        # ==========================

        retrieval_results = self.retriever.search(
            query=query,
            top_k=10
        )

        docs = retrieval_results

        print(f"\nRetrieved {len(docs)} documents")

        # ==========================
        # RE-RANKING
        # ==========================

        reranked_docs = self.reranker.rerank(
            query=query,
            docs=docs,
            top_k=3
        )

        print(f"Re-ranked to {len(reranked_docs)} documents")

        # ==========================
        # PROMPT BUILDING
        # ==========================

        prompt = PromptBuilder.build_prompt(
            query=query,
            docs=reranked_docs,
            history=history
        )

        # ==========================
        # LLM GENERATION
        # ==========================

        response = self.llm.generate(prompt)

        # ==========================
        # FINAL OUTPUT
        # ==========================

        return {
            "query_analysis": query_info,
            "retrieved_docs": reranked_docs,
            "answer": response
        }