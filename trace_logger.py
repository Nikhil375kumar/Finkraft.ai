logs = []

def log_trace(entry: str):
    logs.append(entry)

def get_traces():
    return logs

#  Driver Code
if __name__ == "__main__":
    print("\n=== Trace Logger Test ===\n")
    log_trace("User: Download report → Action")
    log_trace("User: Upload issue → Support ticket")
    print("Logs:", get_traces())
