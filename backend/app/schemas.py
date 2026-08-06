from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):  # request body -> user input + validated by pydantic
    title: str = Field(min_length=1, max_length=100)
    related: int | None = Field(default=None, ge=1)


class Task(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )  # allows pydantic response could access ORM

    id: int
    title: str
    completed: bool = False
    related: int | None = None


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    completed: bool | None = Field(default=None)
