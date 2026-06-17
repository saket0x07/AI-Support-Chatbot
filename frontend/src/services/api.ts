import { Message, Conversation, Ticket, AnalyticsOverview } from '../types/chat';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

export const chatApi = {
  async sendMessage(sessionId: string, text: string): Promise<any> {
    const res = await fetch(`${API_BASE_URL}/chat/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: sessionId, message: text }),
    });
    if (!res.ok) throw new Error('Failed to send message');
    return res.json();
  },

  async getHistory(sessionId: string): Promise<Conversation> {
    const res = await fetch(`${API_BASE_URL}/chat/history/${sessionId}`);
    if (!res.ok) throw new Error('Failed to load history');
    return res.json();
  },

  async getTickets(): Promise<Ticket[]> {
    const res = await fetch(`${API_BASE_URL}/tickets/`);
    if (!res.ok) throw new Error('Failed to fetch tickets');
    return res.json();
  },

  async updateTicket(ticketId: number, status: string): Promise<Ticket> {
    const res = await fetch(`${API_BASE_URL}/tickets/${ticketId}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status }),
    });
    if (!res.ok) throw new Error('Failed to update ticket');
    return res.json();
  },

  async getAnalytics(): Promise<AnalyticsOverview> {
    const res = await fetch(`${API_BASE_URL}/analytics/overview`);
    if (!res.ok) throw new Error('Failed to fetch analytics');
    return res.json();
  },

  async ingestDocument(title: string, content: string, category: string, sourceUrl?: string): Promise<any> {
    const res = await fetch(`${API_BASE_URL}/documents/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, content, category, source_url: sourceUrl }),
    });
    if (!res.ok) throw new Error('Failed to ingest document');
    return res.json();
  }
};
