from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task as TaskModel
from app.schemas import (
    Task as TaskSchema,
    TaskCreate,
    TaskUpdate,
)

DatabaseSession = Annotated[Session, Depends(get_db)]

#tasks endpoint

router = APIRouter(
    prefix = "/tasks",
    tags = ["Tasks"],
)

tasks: list[TaskSchema] = []
next_task_id = 1

@router.post("",
          response_model=TaskSchema, #response yang dikembalikan dari backend
          status_code=status.HTTP_201_CREATED)

def create_task(task_data: TaskCreate, db: DatabaseSession) -> TaskModel:
    """creates ORM OBJECT"""
    task = TaskModel(
        title=task_data.title,
        completed=False,
        related=task_data.related,
    )

    """DB session start"""
    db.add(task)

    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise

    db.refresh(task)

    return task

@router.get("", response_model=list[TaskSchema])

def get_task() -> list[TaskSchema]:
    return tasks

@router.get(
        "/{task_id}", 
        response_model=TaskSchema)

def get_task_id(task_id:int) -> TaskSchema:
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Task not found")

@router.patch("/{task_id}", response_model=TaskSchema)

def update_task(task_id:int, task_data:TaskUpdate) -> TaskSchema:
    update_data= task_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one field must be provided",
        )

    if "title" in update_data and update_data["title"] is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be null",
        )

    if "completed" in update_data and update_data["completed"] is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Completed cannot be null"
        )

    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.model_copy(update=update_data)

            tasks[index] = updated_task
            return updated_task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )

@router.delete("/{task_id}", 
               status_code=status.HTTP_204_NO_CONTENT)

def delete_task(task_id: int) -> Response:
    for index, task in enumerate(tasks):
            if task.id == task_id:
                tasks.pop(index)

                return Response(status_code=status.HTTP_204_NO_CONTENT) 

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Task cannot be found")
