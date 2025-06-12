
# 🧠 FastAPI + Gradio Chatbot with LLaMA 3 via Ollama

![App Running Screenshot](image/Running.png)

This project combines a FastAPI backend and a Gradio frontend to send prompts to the [LLaMA 3](https://ollama.com/library/llama3) model using [Ollama](https://ollama.com).

---

## 🚀 Requirements

- Python 3.8+
- [Ollama installed](https://ollama.com/download)
- LLaMA 3 model pulled via Ollama

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/quochn-RisingStar/FastAPI-Chat-API-with-LLaMA-3.git
cd my-ai-agent
```

### 2. Create and Activate a Virtual Environment

```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn gradio requests
```

---

## 🧠 Run the LLaMA 3 Model with Ollama

```bash
ollama pull llama3
ollama run llama3
```

> ✅ Ollama serves the model by default at `http://localhost:11434`.

---

## 🚀 Start the App (Backend + UI)

```bash
python3 app.py
```

> 🟢 This will:
>
> * Start a FastAPI backend at: `http://127.0.0.1:8000`
> * Open a Gradio web UI at: [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## 🧪 Test the API

```bash
curl -X POST http://localhost:8000/ask/stream \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Xin chào"}'
```

> 🗨️ The API streams back the LLaMA 3 response using FastAPI's `StreamingResponse`.

---

## 📁 Project Structure

```
my-ai-agent/
├── app.py               # Main entry point (FastAPI + Gradio)
├── README.md
└── requirements.txt
```

---

## ✅ `requirements.txt`

```txt
fastapi
uvicorn
gradio
requests
```

---

## 💡 Ideas for Expansion

* ✅ Add prompt/response memory
* ✅ Add user chat history with timestamps
* 🔒 Add API key or token authentication
* 📊 Monitor usage (requests per user)
* 🧱 Add SQLite/MongoDB to store conversations

---