# 🚀 Gen-AI Playground (LangChain + Azure OpenAI)

This repository documents my hands-on exploration of **LLM systems, tool calling, and agent design using LangChain**.

Instead of relying on pre-built abstractions, I focused on understanding **how things work under the hood** — building components manually and then layering structured applications on top.

---

## 🧠 What this repo covers

This is not a single project — it's a **progressive learning + building repo** covering:

- 🔧 Manual LLM tool-calling orchestration (agent internals)
- 🌐 Integration with external tools (Wikipedia, Tavily Search)
- 💬 Stateful conversational apps using Streamlit
- ⚙️ Azure OpenAI integration via LangChain
- 🧩 Prompt pipelines using LCEL (`prompt | model | parser`)
- 🧪 Debuggable message-driven workflows

---

## 📁 Project Structure
Gen-AI/
│
├── Langchain/
│ ├── QA-ChatBot.py # Streamlit-based chatbot
│ ├── manual_tool_calling_agent.ipynb # Custom agent loop (core learning)
│
├── main.py # Entry / experimentation
├── pyproject.toml # Dependency management (uv)
├── requirements.txt # Backup dependency list
├── .gitignore
└── README.md

---

## 🤖 1. Streamlit QA Chatbot

A simple but clean conversational chatbot built using:

- **Streamlit UI**
- **Azure OpenAI (GPT-4o / GPT-4.1-mini)**
- **LangChain LCEL pipeline**

### ✨ Features

- Model selection from UI
- Streaming responses (token-by-token)
- Persistent conversation using `session_state`
- Clean separation of prompt → model → parser
- Environment-based configuration via `.env`

### ⚙️ Core Flow
User Input → Prompt Template → AzureChatOpenAI → Output Parser → UI Stream

---

## 🧠 2. Manual Tool-Calling Agent (Core Highlight)

📌 File: `manual_tool_calling_agent.ipynb`

This is the **most important part of the repo**.

Instead of using LangChain agents, I implemented the full loop manually:

- LLM decides actions (`tool_calls`)
- Python executes tools
- Results returned via `ToolMessage`
- Loop continues until final answer

---

### 🔁 Execution Flow
User → LLM → Tool Calls → Tool Execution → LLM → ... → Final Answer

---

### 🔧 Capabilities

- Custom tools (`add`, `multiply`)
- External tools:
  - Wikipedia
  - Tavily Search
- Dynamic tool routing
- Multi-step reasoning
- Error handling for tool failures
- Full message trace for debugging

---

### 💡 Why this matters

This implementation demonstrates:

- How LLMs **plan vs execute**
- How **tool calling actually works internally**
- How LangChain agents are structured under the hood
- How to build your own **agent runtime**

👉 This is essentially a **manual ReAct-style agent implementation** :contentReference[oaicite:0]{index=0}

---

## ⚙️ Tech Stack

- **Python 3.12**
- **LangChain**
- **Azure OpenAI**
- **Streamlit**
- **Tavily Search API**
- **Wikipedia API**
- **uv** (fast Python package manager)

---

## 🛠️ Setup Instructions

### 1. Clone repo

```bash
git clone https://github.com/BrainTeaser1/Gen-AI.git
cd Gen-AI

2. Install dependencies (using uv)
uv sync
or
uv pip install -r requirements.txt

3. Create .env
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
TAVILY_API_KEY=your_key_here

4. Run Streamlit App
streamlit run Langchain/QA-ChatBot.py 

(OR)
(just be inside the Langchain folder as your working direcotry. and then just 
streamlit run AQ-ChatBot.py)

Security Note
.env is ignored via .gitignore
No secrets are stored in the repository
API keys must be configured locally

🚧 Current Status
✅ Manual tool-calling agent implemented
✅ Multi-tool reasoning loop working
✅ Streamlit chatbot UI built
✅ Azure OpenAI integration complete

💬 Author

Krishna Shukla

Exploring:
LLM Systems
Agent Architectures
GenAI Infrastructure


