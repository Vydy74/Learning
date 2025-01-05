from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from sqlalchemy import select, insert, update, delete

from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    return task

@router.post("/create")
async def create_task(task_data: CreateTask, db: Annotated[Session, Depends(get_db)]):
    # Проверяем наличие пользователя
    user = db.scalar(select(User).where(User.id == int(task_data.user_id)))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    db.execute(insert(Task).values(title=task_data.title,
                                   content=task_data.content,
                                   priority=task_data.priority,
                                   complited=task_data.complited,
                                   user_id=task_data.user_id,
                                   slug=slugify(task_data.title)))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "Successful"
    }

@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    updated_task = select(Task).where(Task.id == task_id)
    task = db.scalar(updated_task)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no category found"
        )
    else:
        pass
    db.execute(update(Task).where(Task.id == task_id).values(
                                   title=update_task.title,
                                   content=update_task.content,
                                   priority=update_task.priority,


                                   slug=slugify(update_task.title)))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "Successful"
    }

@router.delete("/delete")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверка
    task_query = select(Task).where(Task.id == task_id)
    task = db.scalar(task_query)
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    # Удаляем task
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Task delete is successful!",
    }
