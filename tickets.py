import json, os

TICKET_FILE = "data/tickets.json"

def _load_tickets():
    if not os.path.exists(TICKET_FILE):
        return []
    try:
        with open(TICKET_FILE, "r") as f:
            data = f.read().strip()
            if not data:
                return []
            return json.loads(data)
    except json.JSONDecodeError:
        return []

def create_ticket(query: str):
    tickets = _load_tickets()
    ticket_id = len(tickets) + 1
    ticket = {"ticket_id": ticket_id, "query": query, "status": "Open", "assigned_to": "Support"}
    tickets.append(ticket)

    os.makedirs("data", exist_ok=True)
    with open(TICKET_FILE, "w") as f:
        json.dump(tickets, f, indent=2)

    return ticket

def list_tickets():
    return _load_tickets()

def get_ticket_status():
    tickets = _load_tickets()
    if not tickets:
        return "No tickets found."
    return f"Ticket #{tickets[-1]['ticket_id']} is {tickets[-1]['status']}"

#  Driver Code
if __name__ == "__main__":
    print("\n=== Tickets Test ===\n")
    t1 = create_ticket("Upload not working")
    print("Created:", t1)
    print("All tickets:", list_tickets())
    print("Latest status:", get_ticket_status())
