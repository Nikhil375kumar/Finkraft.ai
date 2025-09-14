import json
from tickets import create_ticket, get_ticket_status
from actions import perform_action
from llm_client import ask_llm  # ✅ use Groq LLM for FAQ answers

def process_query(query: str, role: str, history: list):
    """
    Intent detection and response pipeline.
    Supports: FAQ, ACTION, SUPPORT, TICKET_STATUS
    Priority: Ticket Status > Support > FAQ > Action > Unknown
    """

    query_lower = query.lower()

    # 1️⃣ Ticket Status Check
    if "status" in query_lower or "ticket" in query_lower:
        return "TICKET_STATUS", get_ticket_status()

    # 2️⃣ Support Ticket Creation
    elif ("not working" in query_lower 
          or "issue" in query_lower 
          or "error" in query_lower 
          or "problem" in query_lower):
        ticket = create_ticket(query)
        return "SUPPORT", f"Created Support Ticket #{ticket['ticket_id']} (Status: {ticket['status']})"

    # 3️⃣ FAQ Check (before ACTION)
    elif ("how" in query_lower 
          or "what" in query_lower 
          or "why" in query_lower):
        # Call LLM for natural explanation
        answer = ask_llm(f"Answer this user question simply: {query}")
        return "FAQ", answer

    # 4️⃣ Action Check
    elif ("filter" in query_lower 
          or "download" in query_lower 
          or "upload" in query_lower 
          or "export" in query_lower):
        return "ACTION", perform_action(query)

    # 5️⃣ Unknown fallback
    else:
        return "UNKNOWN", "Sorry, I couldn’t understand that."


# ✅ Driver Test
if __name__ == "__main__":
    print("\n=== Pipeline Test ===\n")
    history = []

    test_queries = [
        "How do I use upload feature?",
        "Filter last month’s report",
        "Download the report",
        "Upload feature not working",
        "What is the status of my ticket?"
    ]

    for q in test_queries:
        intent, response = process_query(q, "User", history)
        print("👉", q)
        print("🤖", intent, "|", response, "\n")
