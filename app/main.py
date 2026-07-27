from fastapi import FastAPI, HTTPException, status

from app.schemas import Task, TaskCreate, TaskUpdate
from app.storage import store

app = FastAPI(title="Task Tracker API")

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    return store.create(title=payload.title, description=payload.description)


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return store.list()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = store.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate) -> Task:
    updated = store.update(
        task_id,
        title=payload.title,
        description=payload.description,
        status=payload.status,
    )
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated
