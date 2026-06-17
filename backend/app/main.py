from fastapi import FastAPI
from app.api.routes import router 

app = FastAPI(
    title="Cloudflow AI Support Chatbot API",
    description="Cloudflow AI chatbot API for customer support",
    version="1.0.0",
    
)
app.include_router(router)
