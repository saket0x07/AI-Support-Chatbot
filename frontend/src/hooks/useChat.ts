import { useState, useEffect, useCallback } from 'react';
import { Message } from '../types/chat';
import { chatApi } from '../services/api';

export function useChat(initialSessionId?: string) {
  const [sessionId, setSessionId] = useState<string>('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Generate or restore session ID
  useEffect(() => {
    if (initialSessionId) {
      setSessionId(initialSessionId);
    } else {
      let storedId = localStorage.getItem('cloudflow_session_id');
      if (!storedId) {
        storedId = `session_${Math.random().toString(36).substring(2, 11)}`;
        localStorage.setItem('cloudflow_session_id', storedId);
      }
      setSessionId(storedId);
    }
  }, [initialSessionId]);

  // Load message history when session is ready
  useEffect(() => {
    if (!sessionId) return;

    const loadHistory = async () => {
      try {
        setLoading(true);
        const history = await chatApi.getHistory(sessionId);
        setMessages(history.messages || []);
        setError(null);
      } catch (err: any) {
        setError(err.message || 'Failed to load history');
      } finally {
        setLoading(false);
      }
    };

    loadHistory();
  }, [sessionId]);

  // Submit user message
  const sendMessage = useCallback(async (text: string) => {
    if (!text.trim() || !sessionId) return;

    // Optimistically append user message
    const userMsg: Message = { role: 'user', content: text };
    setMessages((prev) => [...prev, userMsg]);

    try {
      setLoading(true);
      setError(null);
      const res = await chatApi.sendMessage(sessionId, text);
      
      const assistantMsg: Message = {
        role: 'assistant',
        content: res.response,
        intent: res.intent,
        sentiment: res.sentiment,
        confidence: res.confidence,
        citations: res.citations
      };
      
      setMessages((prev) => [...prev, assistantMsg]);
    } catch (err: any) {
      setError(err.message || 'Failed to send message');
    } finally {
      setLoading(false);
    }
  }, [sessionId]);

  const clearSession = useCallback(() => {
    const newId = `session_${Math.random().toString(36).substring(2, 11)}`;
    localStorage.setItem('cloudflow_session_id', newId);
    setSessionId(newId);
    setMessages([]);
  }, []);

  return {
    sessionId,
    messages,
    loading,
    error,
    sendMessage,
    clearSession
  };
}
