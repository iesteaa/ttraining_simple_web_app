from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.orm import Session

from alembic import command
from alembic.config import Config

BACKEND_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BACKEND_ROOT.parent
TEST_ENV_FILE = PROJECT_ROOT / ".env.test"

# Local development uses .env.test.
# CI can supply the same values directly as environment variables.
if TEST_ENV_FILE.exists():
    load_dotenv(TEST_ENV_FILE, override=True)


# These imports must happen after loading the test environment.
from app.config import settings  # noqa: E402
from app.database import engine, get_db  # noqa: E402
from main import app  # noqa: E402

EXPECTED_TEST_DATABASE = "task_app_test_db"

if settings.postgres_db != EXPECTED_TEST_DATABASE:
    raise RuntimeError(
        "Automated tests were stopped for safety. "
        f"Expected database '{EXPECTED_TEST_DATABASE}', "
        f"but received '{settings.postgres_db}'."
    )


@pytest.fixture(scope="session", autouse=True)
def migrated_test_database() -> Generator[None, None, None]:
    """Apply all Alembic migrations before running the test session."""

    alembic_config = Config(str(BACKEND_ROOT / "alembic.ini"))
    alembic_config.set_main_option(
        "script_location",
        str(BACKEND_ROOT / "alembic"),
    )

    command.upgrade(alembic_config, "head")

    # Establish a predictable baseline at the start of the suite.
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE tasks RESTART IDENTITY CASCADE"))

    yield

    engine.dispose()


@pytest.fixture
def db_session(
    migrated_test_database: None,
) -> Generator[Session, None, None]:
    """Provide one isolated database transaction for each test."""

    connection = engine.connect()
    outer_transaction = connection.begin()

    session = Session(
        bind=connection,
        join_transaction_mode="create_savepoint",
    )

    try:
        yield session
    finally:
        session.close()

        if outer_transaction.is_active:
            outer_transaction.rollback()

        connection.close()


@pytest.fixture
def client(
    db_session: Session,
) -> Generator[TestClient, None, None]:
    """Use the isolated test Session for FastAPI requests."""

    def override_get_db() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
