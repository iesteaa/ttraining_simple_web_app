from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.orm import Session


def test_openapi_document_is_available(
    client: TestClient,
) -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "/tasks" in response.json()["paths"]


def test_test_database_is_used(
    db_session: Session,
) -> None:
    database_name = db_session.scalar(
        text("SELECT current_database()")
    )

    assert database_name == "task_app_test_db"
