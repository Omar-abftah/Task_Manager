from typing import List, Optional
from schemas.tasks_schema import TaskCreate, Task, TaskUpdate


tasksList = []

def find_task(id)-> Task|None:
    return next((task for task in tasksList if task.id == id), None)

def find_task_index(id)-> int|None:
    for index, task in enumerate(tasksList):
        if task.id == id:
            return index
    return None

def create(task)-> Task:
    new_id = max(task.id for task in tasksList) + 1 if tasksList else 1
    new_task = Task(id=new_id,
                   name=task.name,
                   priority=task.priority,
                   status=task.status
                   )
    tasksList.append(new_task)
    return new_task

def all_tasks(status, limit)-> List[Task]:
    sorted_list = sorted(tasksList)
    if status is not None:
        sorted_list = [task for task in sorted_list if task.status == status]
    if limit is not None:
        sorted_list = sorted_list[:limit]
    return sorted_list

def get_task(id) -> Task|None:
    return find_task(id)

def update_task(id, updated_task)-> Task|None:
    task = find_task(id)
    if task is None:
        return None
    task.name = updated_task.name if updated_task.name else task.name
    task.priority = updated_task.priority if updated_task.priority else task.priority
    task.status = updated_task.status if updated_task.status else task.status
    return task


def delete_task(id)-> Task|None:
    index = find_task_index(id)
    if index is None:
        return None
    deleted_task = tasksList.pop(index)
    return deleted_task

