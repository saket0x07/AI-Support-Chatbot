# CloudFlow AI Support Assistant

An AI-powered customer support chatbot for a SaaS company (CloudFlow). Answer support queries using Retrieval-Augmented Generation (RAG), classifies intent and sentiment, tracks session memory, and escalates unresolved questions to human support tickets.

## System Architecture

```
User Message
      ↓
Chat API (FastAPI)
      ↓
Chat Service
      ↓
Intent Classifier
      ↓
Sentiment Analyzer
      ↓
Retriever (ChromaDB Vector DB)
      ↓
Prompt Builder
      ↓
LLM (Gemini / OpenAI)
      ↓
Confidence Check
      ↓
Ticket Escalation (optional, saved to SQLite)
      ↓
Response to User
```

## Folder Structure

- `backend/`: FastAPI application containing API routes, RAG operations, NLP helpers, and Database connections.
- `frontend/`: Next.js application presenting the customer chat interface, conversation logs, and support metrics dashboard.
- `docker/`: Docker configurations.
- `docs/`: API and schema design documentation.

## Running Locally

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```
2. Create virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set up environment:
   ```bash
   cp .env.example .env
   # Add your API keys inside .env
   ```
4. Run server:
   ```bash
   python -m app.main
   ```

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```
2. Install packages and run dev server:
   ```bash
   npm install
   npm run dev
   ```

### Run using Docker Compose

```bash
docker-compose up --build
```
This launches the FastAPI and Next.js containers.
