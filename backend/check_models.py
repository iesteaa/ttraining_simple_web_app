from sqlalchemy import inspect

from app.database import Base, engine
from app.models import Task

# Check if task table(models) registered in Base.metadata(DeclarativeBase)
def main() -> None:
    print(f"ORM class: {Task.__name__}")
    print(f"Mapped table: {Task.__tablename__}")
    print(f"Registered tables: {list(Base.metadata.tables.keys())}")
    print()

    task_table = Base.metadata.tables["tasks"]

    print("Columns:")

    for column in task_table.columns:
        print(
            f"- name={column.name}, "
            f"type={column.type}, "
            f"primary_key={column.primary_key}, "
            f"nullable={column.nullable}"
        )

    database_inspector = inspect(engine)

    print()
    print(
        "Table exists in PostgreSQL:",
        database_inspector.has_table("tasks", schema="public"),
    )


if __name__ == "__main__":
    main()
