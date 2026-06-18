import sqlite3
import pandas as pd
import streamlit as st
from pathlib import Path

# Resolve path to backend/memory.db relative to this file
db_path = Path(__file__).resolve().parents[1] / "backend" / "memory.db"

conn=sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM feedback ORDER BY timestamp DESC", conn)

st.title("Feedback Dashboard")
st.dataframe(df, width="stretch")
