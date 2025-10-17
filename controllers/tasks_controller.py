from fastapi import HTTPException
from schemas.tasks_schema import TaskCreate, Task, TaskUpdate, Status
from services import tasks_service as ts
from typing import Optional, List


def create_tasks(task: TaskCreate)-> Task:
    return ts.create(task)

def get_all_tasks(status: Optional[Status] = None, limit: Optional[int] = None)-> List[Task]:
    return ts.all_tasks(status, limit)

def get_task(id)-> Task:
    task = ts.get_task(id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def delete_task(id)-> Task:
    task = ts.delete_task(id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task(id, updated_task: TaskUpdate)-> Task:
    task = ts.update_task(id, updated_task)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task