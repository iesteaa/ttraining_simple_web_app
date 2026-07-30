from sqlalchemy import Boolean, String, false
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


# Define table structure in ORM form
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=false(),
    )

    related: Mapped[int | None] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (
            f"Task(id={self.id!r}, "
            f"title={self.title!r}, "
            f"completed={self.completed!r}), "
            f"related task={self.related!r})"
        )
