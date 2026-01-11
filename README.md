Tested with Python 3.12.
Local AI Assistant (LangChain + Ollama + FastAPI)

A fully local, free AI assistant built with LangChain, Ollama, and FastAPI, designed to demonstrate how real assistants should be built — without fragile agents, slow RAG pipelines, or paid APIs.

This project focuses on:

Correct intent routing

Clear tool boundaries

Predictable behavior

Fast local inference (CPU-friendly)

✨ Features

✅ Runs 100% locally (no OpenAI, no cloud)

✅ Uses Ollama (e.g. llama3.2)

✅ Clean intent map (no agent chaos)

✅ Wikipedia lookup for factual entities

✅ Reasoned answers for comparative questions

✅ Conversation memory (session-based)

✅ FastAPI backend with Swagger UI

✅ CLI mode + API mode

✅ Designed as a learning project

🧭 Why this project exists

Many LangChain tutorials jump straight into agents and RAG, which often leads to:

Infinite loops

Hallucinations

Dependency conflicts

Slow inference

Hard-to-debug behavior

This project takes a different approach:

Start with a robust assistant.
Add agents only when truly needed.

This mirrors how real production AI systems are designed.

🧠 Architecture Overview
User
 ├─> Intent Router
 │     ├─ time        → deterministic tool
 │     ├─ entity      → Wikipedia
 │     ├─ comparison  → constrained LLM reasoning
 │     └─ open        → LLM + memory
 │
 └─> Response


No agent loops.
No uncontrolled tool calls.
Everything is explicit.

🧩 Intent Map
Intent	Description	Example
time	Date/time queries	“What time is it?”
entity	Encyclopedic lookup	“Who is Alan Turing?”
comparison	Reasoned factual questions	“Warmest country in Europe?”
open	Conversational / explanatory	“Explain black holes”

🚀 Getting Started
1️⃣ Create environment
conda create -n langchain_agent python=3.12
conda activate langchain_agent

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start Ollama
ollama serve
ollama pull llama3.2

💬 Run in CLI mode
python assistant.py


Example:

You: What are the warmest countries in Europe?
🤖 Cyprus, Greece, and southern Spain are generally considered the warmest...

🌐 Run as a Local API
python api.py


Open in browser:

http://127.0.0.1:8000/docs


Test via Swagger UI.

📡 API Example
Request
{
  "message": "Who is Ada Lovelace?",
  "session_id": "student1"
}

Response
{
  "reply": "📚 Source: Wikipedia\n\nAda Lovelace was an English mathematician..."
}

🧠 Memory Model

Session-based memory using session_id

Stored in-process (simple, fast, transparent)

Designed for learning — not production persistence

❌ What this project does NOT do (by design)

❌ No autonomous agents

❌ No uncontrolled tool loops

❌ No heavy RAG pipelines

❌ No paid APIs

❌ No embeddings by default

These are intentional tradeoffs for clarity and reliability.

🔄 Assistant vs Agent (Important)
Assistant	Agent
Explicit routing	Autonomous planning
Predictable	Hard to debug
Fast	Often slow
Beginner-friendly	Easy to misuse
Production-aligned	Demo-oriented

This project proves you can build useful AI systems without agents.

📚 Learning Outcomes

By studying this repo, you will learn:

How intent routing works

When not to use RAG

Why agents often fail beginners

How real assistants are structured

How to combine tools + LLM safely

🛠️ Future Extensions (Optional)

Lightweight retrieval (hybrid RAG-lite)

Source attribution per answer

Persistent memory (SQLite / Redis)

Agent comparison demo

Frontend UI

👨‍🎓 Project Context

Built as a student learning project, inspired by experimentation with:

LangChain

Ollama

FastAPI

Modern AI engineering practices

📜 License

MIT — use freely, learn freely.
