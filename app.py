import streamlit as st
from pipeline import process_query
from context_manager import load_memory, add_to_history
from role_manager import filter_tickets_by_role
from trace_logger import log_trace, get_traces

def run_app():
    st.set_page_config(page_title="Unified In-App Assistant", layout="wide")
    st.title("🤖 Unified In-App Assistant")

    role = st.sidebar.selectbox("Select Role", ["Manager", "User", "Intern"])
    memory = load_memory()

    # Sidebar panels
    st.sidebar.subheader("📜 History")
    for msg in memory["history"]:
        st.sidebar.write(f"🧑: {msg['query']}")
        st.sidebar.write(f"🤖: {msg['response']}")

    st.sidebar.subheader("🎫 Tickets")
    for t in filter_tickets_by_role(role):
        st.sidebar.write(f"#{t['ticket_id']} - {t['query']} ({t['status']})")

    st.sidebar.subheader("🔍 Logs")
    for log in get_traces():
        st.sidebar.write(log)

    # === Main chat area ===
    st.subheader("💬 Chat Conversation")

    # Display full conversation from memory
    for msg in memory["history"]:
        with st.chat_message("user"):
            st.write(msg["query"])
        with st.chat_message("assistant"):
            st.write(msg["response"])

    # Chat input (new message)
    query = st.chat_input("Type your message...")
    if query:
        intent, response = process_query(query, role, memory["history"])
        add_to_history(query, response)
        log_trace(f"{role} asked: {query} → {intent}")

        # Display new messages immediately
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            st.write(response)

# ✅ Streamlit entry point
if __name__ == "__main__":
    run_app()
