from fastapi import FastAPI
from backend.orchestrator import run_orchestrator

app = FastAPI()

@app.post("/run-orchestrator")
def run():
    return run_orchestrator()
