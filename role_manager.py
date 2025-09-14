from tickets import list_tickets

def filter_tickets_by_role(role):
    tickets = list_tickets()
    if role == "Manager":
        return tickets
    elif role == "User":
        return [t for t in tickets if t["assigned_to"] == "Support"]  # mock filter
    else:
        return []  # Intern has no access
