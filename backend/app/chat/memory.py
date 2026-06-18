from app.chat.sqlite_memory import SQLiteMemory


class MemoryService:

    def __init__(self):
        self.memory = SQLiteMemory()

    def get_history(
        self,
        session_id: str
    ):
        return self.memory.get_history(session_id)

    def get_recent_history(
        self,
        session_id: str,
        limit: int = 10
    ):
        history = self.memory.get_history(session_id)
        return history[-limit:]

    def add_user_message(
        self,
        session_id: str,
        message: str
    ):
        self.memory.add_message(
            session_id,
            "user",
            message
        )

    def add_assistant_message(
        self,
        session_id: str,
        message: str
    ):
        self.memory.add_message(
            session_id,
            "assistant",
            message
        )

    def clear_history(
        self,
        session_id: str
    ):
        self.memory.clear_history(session_id)

    def close(self):
        self.memory.close()

    def add_feedback(self,session_id,query,answer,rating):
        self.memory.add_feedback(session_id,query,answer,rating)

    def get_feedback(self):
        return self.memory.get_feedback()


# class ConversationMemory:
#     def __init__(self):
#         self.sessions={}

#     def add_message(self,session_id:str,role:str,content:str):
#         if session_id not in self.sessions:
#             self.sessions[session_id] = []
            
#         self.sessions[session_id].append({
#             "role": role,
#             "content": content,
#         })

#     def get_history(self,session_id:str):
#         return self.sessions.get(session_id,[])

#     def get_recent_history(self,session_id:str,limit:int=10) -> list:
#         history = self.get_history(session_id)
#         return history[-limit:]



#     def clear_history(self,session_id:str):
#         if session_id in self.sessions:
#             del self.sessions[session_id]  