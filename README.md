# 🚀 Gen-AI Playground (LangChain + Azure OpenAI)

This repository documents my hands-on exploration of **LLM systems, tool calling, and agent design using LangChain**.

Instead of relying on high-level abstractions, this repo focuses on **understanding how things work under the hood** — building components manually and then layering applications on top.

---

## 🧠 What this repo covers

* 🔧 Manual LLM tool-calling orchestration (agent internals)
* 🌐 Integration with external tools (Wikipedia, Tavily Search)
* 💬 Stateful conversational apps using Streamlit
* ⚙️ Azure OpenAI integration via LangChain
* 🧩 Prompt pipelines using LCEL (`prompt | model | parser`)
* 🧪 Debuggable message-driven workflows

---

## 📁 Project Structure

```
Gen-AI/
│
├── Langchain/
│   ├── QA-ChatBot.py
│   └── manual_tool_calling_agent.ipynb
│
├── main.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🤖 Streamlit QA Chatbot

A simple conversational chatbot built using:

* Streamlit UI
* Azure OpenAI (GPT-4o / GPT-4.1-mini)
* LangChain LCEL pipeline

### ✨ Features

* Model selection from UI
* Streaming responses (token-by-token)
* Persistent conversation using `session_state`
* Prompt → Model → Parser pipeline
* Environment-based configuration via `.env`

### ⚙️ Flow

```
User Input → Prompt Template → AzureChatOpenAI → Output Parser → UI
```

---

## 🧠 Manual Tool-Calling Agent (Core Highlight)

File: `manual_tool_calling_agent.ipynb`

This is the core learning component where the full agent loop is implemented manually:

1. User query sent to LLM
2. LLM returns `tool_calls`
3. Tools executed manually in Python
4. Results returned via `ToolMessage`
5. Loop continues until final answer

### 🔁 Flow

```
User → LLM → Tool Calls → Tool Execution → LLM → Final Answer
```

### 🔧 Capabilities

* Custom tools (`add`, `multiply`)
* External tools (Wikipedia, Tavily)
* Dynamic tool routing
* Multi-step reasoning
* Error handling
* Full message trace for debugging

---

## ⚙️ Tech Stack

* Python 3.12
* LangChain
* Azure OpenAI
* Streamlit
* Tavily API
* Wikipedia API
* uv (package manager)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/BrainTeaser1/Gen-AI.git
cd Gen-AI
```

### 2. Install dependencies (using uv)

```
uv sync
```

or

```
uv pip install -r requirements.txt
```

### 3. Create `.env`

```
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
TAVILY_API_KEY=your_key_here
```

### 4. Run the Streamlit App

```
streamlit run Langchain/QA-ChatBot.py
```

---

## 🔐 Security Note

* `.env` is ignored via `.gitignore`
* No secrets are stored in the repository
* API keys must be configured locally

---

## 🚧 Current Status

* ✅ Manual tool-calling agent implemented
* ✅ Multi-tool reasoning loop working
* ✅ Streamlit chatbot UI built
* ✅ Azure OpenAI integration complete

---

## 🔭 What's Next

* LangGraph-based orchestration
* Memory (short + long term)
* RAG integration
* Observability (logging, token tracking)
* Tool reliability improvements

---

## 👤 Author

Krishna Shukla

Exploring:

* LLM Systems
* Agent Architectures
* GenAI Infrastructure

---

## ⭐ Final Note

This repository focuses on **understanding before abstraction**.

Instead of relying on built-in agents, I implemented the core loop manually — making it easier to debug, extend, and reason about system behavior.
