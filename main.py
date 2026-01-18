from fastapi import BackgroundTasks
from backend import orchestrator


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status":"backend alive"}
@app.post("/run-orchestrator")
def run_orchestrator_endpoint(background_tasks: BackgroundTasks):
    background_tasks.add_task(orchestrator.run_orchestrator)
    return {"status": "Orchestrator triggered"}
