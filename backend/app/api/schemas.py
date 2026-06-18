from pydantic import BaseModel

class ChatRequest(BaseModel):
    message:str
    session_id:str


class ChatResponse(BaseModel):
    answer:str
    intent:str
    sentiment: str
    sources: list[str]

class FeedbackRequest(BaseModel):
    session_id:str
    query:str
    answer:str
    rating:str