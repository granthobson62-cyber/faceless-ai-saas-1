from fastapi import FastAPI
import backend.orchestrator as orchestrator

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/run-orchestrator")
def run():
    orchestrator.run_orchestrator()
    return {"status": "orchestrator started"}
