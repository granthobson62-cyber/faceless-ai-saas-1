from fastapi import FastAPI, BackgroundTasks
import sys
import os

# Ensure repo root is in Python path (RENDER FIX)
sys.path.insert(0, os.path.dirname(__file__))

import backend.orchestrator as orchestrator


app = FastAPI()

@app.get("/")
def health():
    return {"status": "backend alive"}

@app.post("/run-orchestrator")
def run_orchestrator_endpoint(background_tasks: BackgroundTasks):
    background_tasks.add_task(orchestrator.run_orchestrator)
    return {"status": "Orchestrator triggered"}
