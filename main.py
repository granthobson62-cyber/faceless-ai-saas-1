from fastapi import FastAPI
from backend.orchestrator import run_orchestrator

app = FastAPI()

@app.post("/run-orchestrator")
def run():
    return run_orchestrator()
import os

@app.get("/env-check")
def env_check():
    return {
        "YOUTUBE_API_KEY": "set" if os.getenv("YOUTUBE_API_KEY") else "missing",
        "YOUTUBE_CHANNEL_ID": "set" if os.getenv("YOUTUBE_CHANNEL_ID") else "missing"
    }
