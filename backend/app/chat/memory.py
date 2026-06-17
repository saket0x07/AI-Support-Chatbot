class ConversationMemory:
    def __init__(self):
        self.sessions={}

    def add_message(self,session_id:str,role:str,content:str):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
            
        self.sessions[session_id].append({
            "role": role,
            "content": content,
        })

    def get_history(self,session_id:str):
        return self.sessions.get(session_id,[])

    def get_recent_history(self,session_id:str,limit:int=10) -> list:
        history = self.get_history(session_id)
        return history[-limit:]



    def clear_history(self,session_id:str):
        if session_id in self.sessions:
            del self.sessions[session_id]  