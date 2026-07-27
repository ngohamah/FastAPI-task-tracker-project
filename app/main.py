from fastapi import FastAPI, status

from app.schemas import Task, TaskCreate
from app.storage import store

app = FastAPI(title="Task Tracker API")

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    return store.create(title=payload.title, description=payload.description)
