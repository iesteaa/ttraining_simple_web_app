from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task as TaskModel
from app.schemas import (
    Task as TaskSchema,
)
from app.schemas import (
    TaskCreate,
    TaskUpdate,
)

DatabaseSession = Annotated[Session, Depends(get_db)]

# tasks endpoint

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post(
    "",
    response_model=TaskSchema,  # response yang dikembalikan dari backend
    status_code=status.HTTP_201_CREATED,
)
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
def get_task(db: DatabaseSession) -> list[TaskModel]:
    statement = select(TaskModel).order_by(TaskModel.id)

    return list(db.scalars(statement).all())


@router.get("/{task_id}", response_model=TaskSchema)
def get_task_id(task_id: int, db: DatabaseSession) -> TaskModel:
    task = db.get(TaskModel, task_id)

    if task is not None:
        return task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.patch("/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task_data: TaskUpdate, db: DatabaseSession) -> TaskModel:
    update_data = task_data.model_dump(exclude_unset=True)

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
            status_code=status.HTTP_400_BAD_REQUEST, detail="Completed cannot be null"
        )

    task = db.get(TaskModel, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    for field, value in update_data.items():
        setattr(task, field, value)

    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise

    db.refresh(task)

    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: DatabaseSession) -> Response:
    task = db.get(TaskModel, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task cannot be found",
        )

    try:
        db.delete(task)
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise

    return Response(status_code=status.HTTP_204_NO_CONTENT)
