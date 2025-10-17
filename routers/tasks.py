from fastapi import APIRouter
from controllers import tasks_controller
from schemas.tasks_schema import TaskCreate, TaskUpdate

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)

@router.get('/show')
def show_all_tasks(limit: int | None = None, status: str | None = None):
    return tasks_controller.get_all_tasks(status, limit)

@router.get('/show/{id}')
def show_task(id: int):
    return tasks_controller.get_task(id)

@router.post('/create')
def create_task(task: TaskCreate):
    return tasks_controller.create_tasks(task)

@router.put('/update/{id}')
def update_task(id: int, task: TaskUpdate):
    return tasks_controller.update_task(id, task)

@router.delete('/delete/{id}')
def delete_task(id: int):
    return tasks_controller.delete_task(id)