def perform_action(query: str) -> str:
    q = query.lower()
    if "filter" in q and "last month" in q:
        return " Report filtered for last month."
    elif "download" in q:
        return " Report downloaded."
    elif "upload" in q:
        return " File uploaded successfully."
    else:
        return " Action not recognized."

#  Driver Code
if __name__ == "__main__":
    print("\n=== Actions Test ===\n")
    print(perform_action("Filter last month’s report"))
    print(perform_action("Download the report"))
    print(perform_action("Upload my file"))
    print(perform_action("Unknown command"))
