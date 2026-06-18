from app.chat.memory import MemoryService
from app.rag.rag_pipeline import RAGPipeline


class ChatService:
    def __init__(self):
        self.memory = MemoryService()
        self.rag_pipeline = RAGPipeline()


    def chat(self,session_id:str,query:str):
        history = self.memory.get_recent_history(session_id)
        answer = self.rag_pipeline.answer(query=query,history=history)
        self.memory.add_user_message(session_id,query)
        self.memory.add_assistant_message(session_id,answer["answer"])
        return answer   
        