from pydantic import BaseModel, Field

class Taskcreate(BaseModel): #request body -> user input + validated by pydantic
    title: str = Field(min_length=1, max_length=100)
    related_task: int = Field(ge=1)

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    related_task: int | None = None

class TaskUpdate(BaseModel):
    title: str | None= Field(default=None, min_length=1, max_length=100)
    completed: bool | None=None
