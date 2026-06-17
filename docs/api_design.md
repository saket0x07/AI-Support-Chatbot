# CloudFlow AI Support Assistant API Design

This document details the REST API endpoints exposed by the CloudFlow support assistant backend.

---

## 1. Chat Endpoints

### Post Message
- **Endpoint**: `POST /api/chat/`
- **Description**: Submit a new message into a conversation session.
- **Request Body**:
  ```json
  {
    "session_id": "session_abc123",
    "message": "How do I reset my password?"
  }
  ```
- **Response Body**:
  ```json
  {
    "session_id": "session_abc123",
    "response": "To reset your password, visit the login page and click 'Forgot Password'.",
    "intent": "Account Management",
    "sentiment": "Neutral",
    "confidence": 0.85,
    "citations": [
      {
        "title": "Account Password Recovery",
        "content": "To reset your password, visit the login page...",
        "category": "Authentication",
        "source_url": "https://docs.cloudflow.com/auth/reset",
        "score": 0.88
      }
    ],
    "ticket_created": false,
    "ticket_id": null
  }
  ```

### Get History
- **Endpoint**: `GET /api/chat/history/{session_id}`
- **Description**: Retrieves history for a session.
- **Response Body**:
  ```json
  {
    "id": 1,
    "session_id": "session_abc123",
    "summary": "User reset password guidance",
    "created_at": "2026-06-16T14:00:00Z",
    "updated_at": "2026-06-16T14:02:00Z",
    "messages": [
      {
        "role": "user",
        "content": "How do I reset my password?",
        "intent": "Account Management",
        "sentiment": "Neutral",
        "confidence": null,
        "citations": null,
        "created_at": "2026-06-16T14:00:00Z"
      }
    ]
  }
  ```

---

## 2. Document Endpoints

### Upload Document
- **Endpoint**: `POST /api/documents/`
- **Description**: Ingests a new article.
- **Request Body**:
  ```json
  {
    "title": "Refund Policy",
    "content": "We offer a 14-day money back guarantee...",
    "category": "Refunds",
    "source_url": "https://docs.cloudflow.com/billing/refunds"
  }
  ```
- **Response Body**:
  ```json
  {
    "id": 12,
    "title": "Refund Policy",
    "content": "We offer a 14-day money back guarantee...",
    "category": "Refunds",
    "source_url": "https://docs.cloudflow.com/billing/refunds",
    "created_at": "2026-06-16T14:00:00Z",
    "updated_at": "2026-06-16T14:00:00Z"
  }
  ```

---

## 3. Ticket Endpoints

### List Tickets
- **Endpoint**: `GET /api/tickets/`
- **Description**: Returns all escalated tickets.

### Patch Ticket
- **Endpoint**: `PATCH /api/tickets/{ticket_id}`
- **Request Body**:
  ```json
  {
    "status": "Resolved"
  }
  ```

---

## 4. Analytics Endpoints

### Overview Dashboard
- **Endpoint**: `GET /api/analytics/overview`
- **Description**: Aggregated summary reports of chat counts, sentiment split, and tickets.
