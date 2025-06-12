from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests

app = FastAPI()

class AskRequest(BaseModel):
    prompt: str

def stream_response(prompt: str):
    try:
        res = requests.post(
            "http://localhost:11435/api/generate",  # Ensure correct port
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
                        import json
                        data = json.loads(line)
                        chunk = data.get("response", "")
                        yield chunk
                    except Exception as e:
                        print("Stream decode error:", str(e))

        return StreamingResponse(generate(), media_type="text/plain")

    except requests.Timeout:
        raise HTTPException(status_code=504, detail="Model timed out. Please try again later.")
    except requests.ConnectionError:
        raise HTTPException(status_code=503, detail="Cannot connect to model server.")
    except Exception as e:
        print("Unhandled error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask/stream")
def ask_model_stream(data: AskRequest):
    return stream_response(data.prompt)
