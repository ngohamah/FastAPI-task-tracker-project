from typing import Optional

from app.schemas import Task, TaskStatus


class TaskStore:
    """In-memory task store. Prototype-scoped: no persistence by design."""

    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def create(self, title: str, description: str) -> Task:
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list(self, status: Optional[TaskStatus] = None) -> list[Task]:
        tasks = list(self._tasks.values())
        if status is not None:
            tasks = [t for t in tasks if t.status == status]
        return tasks

    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update(self, task_id: int, **fields) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        updated = task.model_copy(update={k: v for k, v in fields.items() if v is not None})
        self._tasks[task_id] = updated
        return updated

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None
