from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator

class Priority(Enum):
    high = 1
    medium = 2
    low = 3

class Status(str, Enum):
    done = 'done'
    not_started = 'not started'
    in_progress = 'in progress'

class TaskBase(BaseModel):
    name: str = Field(..., description='Task Name')
    priority: Priority = Field(..., description='Task Priority')
    status: Status = Field(..., description='Staus of the task')

class Task(TaskBase):
    id: int = Field(..., description='Task ID')

    def __lt__(self, other):
        return self.priority.value < other.priority.value if self.priority.value != other.priority.value else self.id < other.id

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    id: Optional[int] = Field(None, description='Task ID')
    name: Optional[str] = Field(None, description='Task Name')
    priority: Optional[Priority] = Field(None, description='Task Priority')
    status: Optional[Status] = Field(None, description='Staus of the task')
