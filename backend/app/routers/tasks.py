from fastapi import APIRouter, status, HTTPException, Response
from app.schemas import Task, Taskcreate, TaskUpdate

#tasks endpoint

router = APIRouter(
    prefix = "/tasks",
    tags = ["Tasks"],
)

tasks: list[Task] = []
next_task_id = 1

@router.post("",
          response_model=Task, #response yang dikembalikan dari backend
          status_code=status.HTTP_201_CREATED)

def create_task(task_data: Taskcreate) -> Task:
    global next_task_id

    new_task = Task(
        id=next_task_id,
        title=task_data.title,
        completed=False,
        related_task=task_data.related_task)

    tasks.append(new_task)
    next_task_id += 1

    return new_task

@router.get("", response_model=list[Task])

def get_task() -> list[Task]:
    return tasks

@router.get(
        "/{task_id}", 
        response_model=Task)

def get_task_id(task_id:int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Task not found")

@router.patch("/{task_id}", response_model=Task)

def update_task(task_id:int, task_data:TaskUpdate) -> Task:
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
