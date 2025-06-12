import threading
import time
import json
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import gradio as gr
import uvicorn

# ----------------------------
# FastAPI backend
# ----------------------------

app = FastAPI()

class AskRequest(BaseModel):
    prompt: str

def stream_response(prompt: str):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": True,
            },
            stream=True,
            timeout=60
        )
        res.raise_for_status()

        def generate():
            for line in res.iter_lines(decode_unicode=True):
                if line:
                    try:
                        data = json.loads(line)
                        chunk = data.get("response", "")
                        yield chunk
                    except Exception as e:
                        print("Stream decode error:", str(e))

        return StreamingResponse(generate(), media_type="text/plain")

    except requests.Timeout:
        raise HTTPException(status_code=504, detail="Model timed out.")
    except requests.ConnectionError:
        raise HTTPException(status_code=503, detail="Cannot connect to model server.")
    except Exception as e:
        print("Unhandled error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask/stream")
def ask_model_stream(data: AskRequest):
    return stream_response(data.prompt)

def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# ----------------------------
# Gradio frontend
# ----------------------------

def call_api(prompt, history=[]):
    try:
        # gọi API FastAPI nội bộ của mày (không trực tiếp model nữa)
        res = requests.post("http://localhost:8000/ask/stream", json={"prompt": prompt})
        res.raise_for_status()
        reply = res.text
    except Exception as e:
        reply = f"Lỗi gọi API: {e}"

    history.append((prompt, reply))
    return "", history

def run_gradio():
    with gr.Blocks() as demo:
        gr.Markdown("# 🤖 Chat với LLaMA 3")
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="Nhập tin nhắn...")
        btn = gr.Button("Gửi")

        msg.submit(call_api, [msg, chatbot], [msg, chatbot])
        btn.click(call_api, [msg, chatbot], [msg, chatbot])

    demo.launch()

# ----------------------------
# Run both
# ----------------------------

if __name__ == "__main__":
    threading.Thread(target=run_fastapi, daemon=True).start()
    time.sleep(1)
    run_gradio()
