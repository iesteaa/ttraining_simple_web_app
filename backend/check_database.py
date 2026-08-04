from app.database import engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


def main() -> None:
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("""
                    SELECT
                        current_database(),
                        current_user
                    """)
            )

            database_name, user_name = result.one()

            print("Database connection successful")
            print(f"Database: {database_name}")
            print(f"User: {user_name}")

    except SQLAlchemyError as error:
        print("Database connection failed")
        print(error)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
