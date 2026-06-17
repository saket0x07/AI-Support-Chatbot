export interface Citation {
  title: string;
  content: string;
  category: string;
  source_url?: string;
  score?: number;
}

export interface Message {
  id?: number;
  role: 'user' | 'assistant' | 'system';
  content: string;
  intent?: string;
  sentiment?: string;
  confidence?: number;
  citations?: Citation[];
  created_at?: string;
}

export interface Conversation {
  id: number;
  session_id: string;
  summary?: string;
  created_at: string;
  updated_at: string;
  messages?: Message[];
}

export interface Ticket {
  id: number;
  conversation_id: number;
  subject: string;
  description: string;
  status: 'Open' | 'In Progress' | 'Resolved' | 'Closed';
  priority: 'Low' | 'Medium' | 'High';
  category?: string;
  created_at: string;
  updated_at: string;
}

export interface IntentDistribution {
  intent: string;
  count: number;
}

export interface SentimentDistribution {
  sentiment: string;
  count: number;
}

export interface TicketStats {
  total_tickets: number;
  open_tickets: number;
  resolved_tickets: number;
}

export interface AnalyticsOverview {
  total_conversations: number;
  total_messages: number;
  intents: IntentDistribution[];
  sentiments: SentimentDistribution[];
  tickets: TicketStats;
}
