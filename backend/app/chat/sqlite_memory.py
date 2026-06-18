import sqlite3

class SQLiteMemory:
    def __init__(self, db_path="memory.db"):
       self.conn = sqlite3.connect(db_path,check_same_thread=False)
       self.create_table()
       
    def create_table(self):
        self.cursor=self.conn.cursor()

        #conversation Memory
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL, 
        role TEXT NOT NULL, 
        content TEXT NOT NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """)

        #Feedback table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            query TEXT NOT NULL,
            answer TEXT NOT NULL,
            rating TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """)
        
        self.conn.commit()

    def add_feedback(self,session_id,query,answer,rating):
        self.cursor.execute("INSERT INTO feedback (session_id,query,answer,rating) VALUES (?,?,?,?)",(session_id,query,answer,rating))
        self.conn.commit()

    def get_feedback(self):
        self.cursor.execute("SELECT * FROM feedback")
        rows=self.cursor.fetchall()
        return [{"id":row[0],"session_id":row[1],"query":row[2],"answer":row[3],"rating":row[4],"timestamp":row[5]} for row in rows]

    def add_message(self,session_id,role,content):
        self.cursor.execute("INSERT INTO conversations (session_id,role,content) VALUES (?,?,?)", (session_id,role,content))
        self.conn.commit()
    
    def get_history(self,session_id,limit=20):
        self.cursor.execute("SELECT role,content FROM conversations WHERE session_id=? ORDER BY id DESC LIMIT ?",(session_id,limit))
        rows=self.cursor.fetchall()
        return [{"role":row[0],"content":row[1]}for row in reversed(rows)]

    def reset_session(self,session_id):
        self.cursor.execute("DELETE FROM conversations WHERE session_id=?",(session_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()