'use client';

import React, { useState, useRef, useEffect } from 'react';
import { useChat } from '../hooks/useChat';

export default function ChatInterface() {
  const { messages, loading, error, sendMessage, clearSession, sessionId } = useChat();
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom of chat
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || loading) return;
    sendMessage(input);
    setInput('');
  };

  const getSentimentEmoji = (sentiment?: string) => {
    switch (sentiment?.toLowerCase()) {
      case 'positive': return '😊';
      case 'negative': return '😠';
      case 'neutral':
      default:
        return '😐';
    }
  };

  return (
    <div className="flex flex-col h-[650px] bg-slate-900 text-slate-100 rounded-2xl shadow-2xl border border-slate-800 overflow-hidden max-w-2xl mx-auto">
      {/* Header */}
      <div className="px-6 py-4 bg-slate-800 border-b border-slate-700 flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-sky-400">CloudFlow Support Assistant</h2>
          <p className="text-xs text-slate-400 font-mono">Session: {sessionId || 'Connecting...'}</p>
        </div>
        <button 
          onClick={clearSession} 
          className="text-xs px-3 py-1.5 bg-slate-700 hover:bg-slate-600 rounded-lg text-slate-300 font-medium transition-colors"
        >
          New Session
        </button>
      </div>

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center space-y-2 text-slate-500">
            <span className="text-4xl">🤖</span>
            <p className="text-sm font-medium text-slate-400">Welcome to CloudFlow Support!</p>
            <p className="text-xs max-w-xs text-slate-500">
              Ask about password resets, billing policies, api keys, or subscriptions.
            </p>
          </div>
        )}

        {messages.map((msg, idx) => (
          <div 
            key={idx} 
            className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'} space-y-1`}
          >
            {/* Metadata (Intent/Sentiment) for Assistant */}
            {msg.role === 'assistant' && (msg.intent || msg.sentiment) && (
              <div className="flex gap-2 px-1 text-[10px] text-slate-400 font-medium">
                {msg.intent && (
                  <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700">
                    Intent: {msg.intent}
                  </span>
                )}
                {msg.sentiment && (
                  <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700 flex items-center gap-1">
                    Sentiment: {getSentimentEmoji(msg.sentiment)} {msg.sentiment}
                  </span>
                )}
              </div>
            )}

            {/* Message Bubble */}
            <div 
              className={`max-w-[85%] px-4 py-3 rounded-2xl text-sm leading-relaxed ${
                msg.role === 'user' 
                  ? 'bg-sky-600 text-white rounded-br-none' 
                  : 'bg-slate-800 text-slate-100 rounded-bl-none border border-slate-700'
              }`}
            >
              <p>{msg.content}</p>
            </div>

            {/* Citations for Assistant Responses */}
            {msg.role === 'assistant' && msg.citations && msg.citations.length > 0 && (
              <div className="mt-2 w-full max-w-md space-y-1 bg-slate-800/50 p-3 rounded-lg border border-slate-700/50">
                <span className="text-[10px] text-slate-400 font-semibold uppercase tracking-wider block">
                  Sources & Citations:
                </span>
                <ul className="text-xs space-y-1 text-sky-400 font-medium">
                  {msg.citations.map((cite, cIdx) => (
                    <li key={cIdx} className="hover:underline">
                      <a href={cite.source_url || '#'} target="_blank" rel="noreferrer" className="flex items-center gap-1">
                        📄 {cite.title} <span className="text-slate-500 font-mono text-[10px]">({Math.round((cite.score || 0) * 100)}% match)</span>
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div className="flex items-center space-x-2 text-slate-400 text-xs py-2">
            <div className="w-2 h-2 bg-sky-500 rounded-full animate-bounce"></div>
            <div className="w-2 h-2 bg-sky-500 rounded-full animate-bounce delay-100"></div>
            <div className="w-2 h-2 bg-sky-500 rounded-full animate-bounce delay-200"></div>
            <span>Support agent is typing...</span>
          </div>
        )}

        {error && (
          <div className="bg-rose-500/10 border border-rose-500/20 text-rose-400 px-4 py-2.5 rounded-lg text-xs">
            Error: {error}
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>

      {/* Input Form */}
      <form onSubmit={handleSend} className="p-4 bg-slate-800/50 border-t border-slate-800 flex gap-2">
        <input 
          type="text" 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          className="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-4 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
          disabled={loading}
        />
        <button 
          type="submit" 
          disabled={loading || !input.trim()}
          className="bg-sky-600 hover:bg-sky-500 disabled:bg-slate-700 text-white rounded-xl px-5 py-2 text-sm font-semibold transition-colors flex items-center justify-center gap-1"
        >
          Send
        </button>
      </form>
    </div>
  );
}
