from fastapi.testclient import TestClient

from app.config import settings

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

"""cors set-up test"""
def test_cors_allows_configured_frontend_origin(
    client: TestClient,
) -> None:
    allowed_origin = settings.cors_origins_list[0]

    response = client.options(
        "/tasks",
        headers={
            "Origin": allowed_origin,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type",
        },
    )

    assert response.status_code == 200
    assert (
        response.headers["access-control-allow-origin"]
        == allowed_origin
    )
    assert "POST" in response.headers[
        "access-control-allow-methods"
    ]


def test_cors_rejects_unknown_origin(
    client: TestClient,
) -> None:
    response = client.options(
        "/tasks",
        headers={
            "Origin": "http://localhost:9999",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type",
        },
    )

    assert response.status_code == 400
    assert "access-control-allow-origin" not in response.headers
