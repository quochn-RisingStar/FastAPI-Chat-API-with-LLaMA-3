

# 🧠 FastAPI Chat API with LLaMA 3 via Ollama

This project provides a simple FastAPI-based API that sends a prompt to the LLaMA 3 language model (via [Ollama](https://ollama.com)) and returns the response — similar to ChatGPT.

---

## 🚀 Requirements

- Python 3.8 or later
- [Ollama installed](https://ollama.com/download)
- LLaMA 3 model pulled via Ollama

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/your-username/my-ai-agent.git
cd my-ai-agent
```
### 2. Create a Virtual Environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Python Dependencies

```bash
pip install fastapi uvicorn requests
```

---

## 🤖 Pull & Run the LLaMA 3 Model

```bash
ollama pull llama3
ollama run llama3
```

> ✅ By default, Ollama will serve the model at `http://localhost:11434`.

---

## 🚦 Start the FastAPI Server

```bash
uvicorn main:app --reload
```

> The server will be available at: `http://127.0.0.1:8000`

---

## 🧪 Test the API Endpoint

Using `curl`:

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hey AI, what is diabetes?"}'
```

> 📌 You’ll get a JSON response with the model's answer.

---

## 📁 Project Structure

```
my-ai-agent/
├── main.py
├── README.md
└── requirements.txt
```

---

## ✅ `requirements.txt` (example)

```txt
fastapi
uvicorn
requests
```

---

## 💡 Suggestions for Improvement

* Add API key authentication
* Build a frontend interface (React, Vue, Flutter)
* Save prompt/response history to SQLite or MongoDB

---