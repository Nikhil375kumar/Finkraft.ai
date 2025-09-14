# Unified In-App Assistant

Demo_Video_ link: https://drive.google.com/drive/folders/1DIho6PpO-KaZvB2nnWh5TiP8EZNLEJH0?usp=sharing

##  Project Overview

This project implements a **Unified In-App Assistant** that customers can use to:

* Perform **product actions** (e.g., filter/download/upload reports).
* Get **plain-English explanations** of features (via LLM).
* Create and track **support tickets**.
* Maintain **conversation context across sessions**.
* Respect **role-based visibility** (Manager, User, Intern).

It combines **rule-based logic** with **Groq LLM** (llama-3.3-70b-versatile) to deliver a conversational experience inside a Streamlit app.

---

##  Project Workflow

### 1. Frontend (Streamlit UI)

* Left Sidebar:

  *  **Select Role** → Manager / User / Intern.
  *  **History** → Shows past conversations (loaded from `memory.json`).
  *  **Tickets** → Displays support tickets (filtered by role).
  *  **Logs** → Displays traces of assistant decisions.

* Main Screen:

  *  **Chat Conversation** → Chat-like view of queries & responses.
  *  **Chat Input** → Type natural language requests.

---

### 2. **Backend Components**

* **`llm_client.py`** → Connects to **Groq LLM** for answering FAQs.
* **`actions.py`** → Executes product actions (`filter`, `download`, `upload`, `export`).
* **`tickets.py`** → Handles support tickets (`create`, `list`, `status`). Stores in `data/tickets.json`.
* **`context_manager.py`** → Stores conversation history in `data/memory.json`.
* **`trace_logger.py`** → Logs actions & intents for transparency.
* **`role_manager.py`** → Filters tickets by role (Manager sees all, User sees own, Intern restricted).
* **`pipeline.py`** → The brain  → routes user queries to correct handler:

  * **FAQ** → Answered by LLM.
  * **ACTION** → Rule-based execution.
  * **SUPPORT** → Ticket created.
  * **TICKET  STATUS** → Ticket lookup.
  * **UNKNOWN** → Fallback message.

---

### 3. **Persistence**

* **`data/memory.json`** → Stores full chat history (for continuity).
* **`data/tickets.json`** → Stores all support tickets.

This ensures the assistant remembers context across sessions.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/unified-inapp-assistant.git
cd unified-inapp-assistant
```

### 2. Create a virtual environment

```bash
conda create -n finkraft python=3.10 -y
conda activate finkraft
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file in the root directory:

```ini
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run pipeline test (CLI)

```bash
python pipeline.py
```

### 6. Launch Streamlit UI

```bash
streamlit run app.py
```

---

##  Example Queries to Test

| Query                              | Expected Intent | Expected Behavior                     |
| ---------------------------------- | --------------- | ------------------------------------- |
| `How do I use upload feature?`     | FAQ             | LLM explains feature in plain English |
| `Filter last month’s report`       | ACTION          | Report filtered                       |
| `Download the report`              | ACTION          | Report downloaded                     |
| `Upload not working`               | SUPPORT         | Support ticket created                |
| `What is the status of my ticket?` | TICKET\_STATUS  | Shows ticket status                   |
| `Tell me a joke`                   | UNKNOWN         | Fallback response                     |

---

##  Role-based Access

* **Manager** → Sees all tickets, logs, history.
* **User (Client)** → Sees only their own tickets & history.
* **Intern** → Restricted view (limited access to tickets/logs).

---

##  Project Flow Diagram

```
User Query → pipeline.py 
    → [FAQ] → llm_client.py (Groq LLM)
    → [ACTION] → actions.py
    → [SUPPORT] → tickets.py (create ticket)
    → [TICKET_STATUS] → tickets.py (get status)
    → [UNKNOWN] → fallback
→ Context saved in context_manager.py
→ Logs stored via trace_logger.py
→ Role filtering applied via role_manager.py
→ Response shown in Streamlit UI
```

---

##  Future Improvements

* Add **ticket update/close functionality**.
* Enhance **role restrictions** (Intern read-only mode).
* Support **multi-user memory** (different users have isolated histories).
* Improve **UI styling** (chat bubbles, colors).

---

##  Deliverable

* **Single Streamlit app (`app.py`)** with sidebar & chat interface.
* **LLM + rule-based hybrid system** for handling user queries.
* **Persistent history & tickets** across sessions.
* **Role-based visibility** implemented.

---
