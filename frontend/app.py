import streamlit as st
import requests
import uuid

API_BASE_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="Chat Support-Assistant",page_icon="🎙️",layout="wide")

st.title("🎙️ Chat Support-Assistant")
st.caption("Intelligent  Chat Support Assistant")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Enter your question")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    payload = {"message":user_input,
    "session_id":st.session_state["session_id"]}
    response = requests.post(API_BASE_URL,json=payload)
    data = response.json()
    answer = data["answer"]
    
    if "sources" in data:
        answer += "\n\n## Sources:"
        for src in data["sources"]:
            answer += f"\n- {src}"

    st.session_state.messages.append({"role":"assistant","content":answer})
    with st.chat_message("assistant"):
        st.markdown(answer)

        col1,col2 = st.columns(2)
        with col1:
            if st.button("Helpful 👍"):
                requests.post("http://localhost:8000/feedback",json={"session_id":st.session_state["session_id"],"query":user_input,"answer":answer,"rating":"positive"})
                st.success("Feedback recorded")
        with col2:
            if st.button("Not Helpful 👎"):
                requests.post("http://localhost:8000/feedback",json={"session_id":st.session_state["session_id"],"query":user_input,"answer":answer,"rating":"negative"})
                st.success("Feedback recorded")