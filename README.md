# AI_Chatbot
Here's a **professional, detailed, and well-structured `README.md`** file for your AI Chatbot project built with FastAPI, LangChain, and Groq:

---

## 🧠 TufanBot – AI Agent Chatbot with FastAPI + Groq + LangChain

Welcome to **TufanBot**, your personal AI assistant powered by **Groq's ultra-fast LLMs** and built using **FastAPI**, **LangChain**, and **Streamlit**. Designed to be production-ready, modular, and developer-friendly, this project lets you create intelligent AI agents that can **chat**, **search the web**, and **respond contextually** to queries.

---

### 🚀 Features

* ⚡ **Groq-powered LLMs** (LLaMA 3.3, Mixtral)
* 🌐 Optional **web search tool** using Tavily (can be disabled)
* 📦 Clean API layer with **FastAPI**
* 🧩 Agent memory and ReAct-style decision making via **LangGraph**
* 💬 Elegant front-end built with **Streamlit**
* 🔑 Uses `.env` for easy API key configuration

---

### 🛠️ Tech Stack

| Layer      | Tools/Frameworks                                   |
| ---------- | -------------------------------------------------- |
| LLM        | [Groq](https://groq.com/), LangChain               |
| Backend    | [FastAPI](https://fastapi.tiangolo.com/)           |
| Frontend   | [Streamlit](https://streamlit.io/)                 |
| Web Search | [Tavily API](https://www.tavily.com/) *(optional)* |
| Deployment | Uvicorn (ASGI Server)                              |

---

### 📁 Folder Structure

```
.
├── ai_agent.py       # AI Agent logic (LLM + tools + agent setup)
├── backend.py        # FastAPI backend for serving responses
├── frontend.py       # Streamlit UI for interacting with the chatbot
├── requirements.txt  # Python dependencies
├── .env              # API keys (GROQ, Tavily)
├── Pipfile & lock    # For pipenv users
└── README.md         # Project overview and instructions
```

---

### 🔧 Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tufanbot-ai-chatbot.git
cd tufanbot-ai-chatbot
```

#### 2. Create `.env` File

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_key  # Optional
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Start the Backend Server

```bash
python backend.py
```

This will run a FastAPI server on `http://127.0.0.1:9999`

#### 5. Launch the Frontend (Streamlit UI)

```bash
streamlit run frontend.py
```

---

### 📸 Demo Screenshots

> <img width="496" height="358" alt="image" src="https://github.com/user-attachments/assets/33d9e9ef-02d8-4edf-a3f8-3ee04fd509ce" />
> <img width="389" height="323" alt="image" src="https://github.com/user-attachments/assets/9fd0e9f5-b8e0-4f41-b023-ce65d968eaa7" />



---

### 📚 API Example

`POST /chat`

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act as a helpful tutor",
  "messages": ["Explain the difference between AI and ML."],
  "allow_search": true
}
```

---

### ✅ Todo / Future Enhancements

* [ ] Add vector memory using FAISS or Pinecone
* [ ] Stream responses from backend
* [ ] User authentication
* [ ] Dockerize the project for deployment

---

### 🙌 Credits

* Built by [Tufan Dey](https://github.com/tufandey)
* Powered by [LangChain](https://www.langchain.com/), [Groq](https://www.groq.com/), [Streamlit](https://streamlit.io/), and [FastAPI](https://fastapi.tiangolo.com/)




