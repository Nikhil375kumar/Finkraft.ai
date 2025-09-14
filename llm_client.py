import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt: str) -> str:
    """Send a prompt to Groq LLM"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

#  Driver Code
if __name__ == "__main__":
    print("\n=== LLM Client Test ===\n")
    answer = ask_llm("Explain what an in-app assistant is in one sentence.")
    print("🤖", answer)
