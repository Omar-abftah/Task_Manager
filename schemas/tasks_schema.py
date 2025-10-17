from typing import Optional

from pydantic import BaseModel, Field, field_validator

class TaskBase(BaseModel):
    name: str = Field(..., description='Task Name')
    priority: str = Field(..., description='Task Priority')
    status: str = Field(..., description='Staus of the task')

    @field_validator('priority')
    def check_if_valid_priority(cls, v):
        if v.lower() not in ['high', 'medium', 'low']:
            raise ValueError('Non acceptable priority')
        return v
    @field_validator('status')
    def check_if_valid_status(cls, v):
        if v.lower() not in ['done', 'in progress', 'not started']:
            raise ValueError('Non acceptable status')
        return v

class TaskCreate(TaskBase):
    pass
class TaskShow(TaskBase):
    id: int = Field(..., description='Task ID')

class TaskUpdate(TaskBase):
    id: Optional[int] = Field(None, description='Task ID')
