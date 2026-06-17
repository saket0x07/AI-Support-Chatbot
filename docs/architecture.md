# CloudFlow AI Support Assistant System Architecture

This document describes the technical architecture and information flow of the CloudFlow AI Support Assistant (V1.0).

## System Flow Overview

The diagram below details the components involved when a user submits a chat message:

```mermaid
sequenceDiagram
    actor User
    participant App as Next.js Frontend
    participant API as FastAPI Backend
    participant NLP as NLP Module (Intent/Sentiment)
    participant Chroma as ChromaDB Vector Store
    participant LLM as Gemini / OpenAI Provider
    participant DB as SQLite DB

    User->>App: Send message "How do I cancel?"
    App->>API: POST /api/chat/ (message, session_id)
    API->>DB: Fetch/Create Conversation Session
    API->>DB: Load previous messages (memory context)
    API->>NLP: Classify intent and analyze sentiment
    NLP-->>API: Intent="Subscription", Sentiment="Neutral"
    API->>DB: Write user message (intent & sentiment)
    API->>Chroma: Query similar chunks for "How do I cancel?"
    Chroma-->>API: Return top-5 documentation paragraphs
    API->>LLM: Generate response (context + prompt + history)
    LLM-->>API: Return generated answer + confidence check
    API->>DB: Write assistant message & citations
    alt Confidence < Threshold
        API->>DB: Generate human escalation support ticket
        API-->>App: Return "Low confidence. Ticket #Created."
    else Confidence >= Threshold
        API-->>App: Return answer + source citations
    end
    App-->>User: Render chatbot bubble + source cards
```

## Key Components

### 1. Backend Service (FastAPI)
The application core that handles routing, database connections, and coordinating LLM and NLP operations.

### 2. Retriever & Vector Database (ChromaDB)
Maintains high-dimensional semantic indexing of CloudFlow help center documents. Queries are mapped to dense vector spaces using Google or OpenAI embeddings.

### 3. NLP Processors
- **Intent Classifier**: Maps messages to specific categories for ticket routing.
- **Sentiment Analyzer**: Captures user urgency or sentiment.
- **Confidence Scorer**: Checks average retrieval scores to confirm grounded answers.

### 4. Memory Store (SQLite via SQLAlchemy)
Maintains persistence for chat histories and created support tickets.
