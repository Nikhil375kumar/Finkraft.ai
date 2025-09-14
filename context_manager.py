import json, os

MEMORY_FILE = "data/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"history": []}
    try:
        with open(MEMORY_FILE, "r") as f:
            data = f.read().strip()
            if not data:  # empty file
                return {"history": []}
            return json.loads(data)
    except json.JSONDecodeError:
        return {"history": []}

def save_memory(memory):
    os.makedirs("data", exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_to_history(query, response):
    memory = load_memory()
    memory["history"].append({"query": query, "response": response})
    save_memory(memory)

#  Driver Code
if __name__ == "__main__":
    print("\n=== Context Manager Test ===\n")
    add_to_history("Filter last month", " Done")
    add_to_history("Download report", " Downloaded")
    print("History:", load_memory())
