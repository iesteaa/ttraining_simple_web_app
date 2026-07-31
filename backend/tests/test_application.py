
from fastapi.testclient import TestClient


def test_openapi_document_is_available(client: TestClient) -> None:
        expected_path = "/tasks"

        response = client.get("/openapi.json")

        assert response.status_code == 200

        response_body = response.json()

        assert "openapi" in response_body
        assert "paths" in response_body
        assert expected_path in response_body["paths"]
