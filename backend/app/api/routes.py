from fastapi import APIRouter
from app.api.schemas import ChatRequest, ChatResponse,FeedbackRequest
from app.chat.chat_service import ChatService
from app.chat.memory import MemoryService



router = APIRouter()

chat_service = ChatService()
memory_service = MemoryService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = chat_service.chat(session_id=request.session_id,query=request.message)
    return ChatResponse(
        answer=response['answer'],
        intent=response['query_analysis']['intent'],
        sentiment=response['query_analysis']['sentiment']['label'],
        sources=response.get('sources', [])
    )

@router.post("/feedback")
def feedback(request: FeedbackRequest):
    memory_service.add_feedback(
        session_id=request.session_id,
        query=request.query,
        answer=request.answer,
        rating=request.rating
    )

    return {
        "status":"success"
    }