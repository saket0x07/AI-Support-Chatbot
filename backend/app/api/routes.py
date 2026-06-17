from fastapi import APIRouter
from app.api.schemas import ChatRequest, ChatResponse
from app.chat.chat_service import ChatService


router = APIRouter()

chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = chat_service.chat(session_id=request.session_id,query=request.message)
    return ChatResponse(
        answer=response['answer'],
        intent=response['query_analysis']['intent'],
        sentiment=response['query_analysis']['sentiment']['label']
    )