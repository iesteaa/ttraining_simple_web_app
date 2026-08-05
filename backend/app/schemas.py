from pydantic import BaseModel, ConfigDict, Field, model_validator


class TaskCreate(BaseModel):  # request body -> user input + validated by pydantic
    title: str = Field(min_length=1, max_length=100)
    related: int | None = Field(default=None, ge=1)


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # allows pydantic response could access ORM

    id: int
    title: str
    completed: bool = False
    related: int | None = None


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    completed: bool | None = Field(default=None)

    @model_validator(mode="after")
    def reject_explicit_nulls(self) -> "TaskUpdate":
        if "title" in self.model_fields_set and self.title is None:
            raise ValueError("title cannot be null")

        if "completed" in self.model_fields_set and self.completed is None:
            raise ValueError("completed cannot be null")

        return self
