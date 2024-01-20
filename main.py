from fastapi import FastAPI, HTTPException
from transformers import pipeline

import os

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

app = FastAPI()



@app.post("/summarize")
async def summarize_text(long_string: str, max_length: int = 130, min_length: int = 30):
    try:
        if not long_string:
            raise HTTPException(status_code=400, detail="long_string is required")

        out_str = summarizer(long_string, max_length=max_length, min_length=min_length, do_sample=False)
        return {"summary": out_str[0]["summary_text"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", 8080))

    gunicorn_command = f"gunicorn -b {host}:{port} main:app"

    # Use Gunicorn if the environment variable indicates it
    use_gunicorn = os.environ.get("USE_GUNICORN", "").lower() == "true"

    if use_gunicorn:
        os.system(gunicorn_command)
    else:
        # Default to Uvicorn if USE_GUNICORN is not set or set to anything other than "true"
        uvicorn_command = f"uvicorn main:app --host {host} --port {port} --reload"
        os.system(uvicorn_command)