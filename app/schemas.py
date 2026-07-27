from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    pending = "pending"
    done = "done"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.pending
