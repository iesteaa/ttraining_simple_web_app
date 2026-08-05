from typing import Any

from fastapi.testclient import TestClient


def create_task(
    client: TestClient,
    title: str = "Learn automated testing",
) -> dict[str, Any]:
    response = client.post(
        "/tasks",
        json={"title": title},
    )

    assert response.status_code == 201

    return response.json()


def test_get_tasks_returns_empty_list(
    client: TestClient,
) -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task(
    client: TestClient,
) -> None:
    response = client.post(
        "/tasks",
        json={"title": "Learn pytest"},
    )

    assert response.status_code == 201

    response_body = response.json()

    assert isinstance(response_body["id"], int)
    assert response_body["title"] == "Learn pytest"
    assert response_body["completed"] is False


def test_create_task_rejects_empty_title(
    client: TestClient,
) -> None:
    response = client.post(
        "/tasks",
        json={"title": ""},
    )

    assert response.status_code == 422


def test_get_tasks_returns_created_tasks_in_id_order(
    client: TestClient,
) -> None:
    first_task = create_task(client, "First task")
    second_task = create_task(client, "Second task")

    response = client.get("/tasks")

    assert response.status_code == 200

    response_body = response.json()

    assert len(response_body) == 2
    assert response_body[0]["id"] == first_task["id"]
    assert response_body[1]["id"] == second_task["id"]
    assert response_body[0]["title"] == "First task"
    assert response_body[1]["title"] == "Second task"


def test_get_existing_task(
    client: TestClient,
) -> None:
    created_task = create_task(client)

    task_id = created_task["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json() == created_task


def test_get_missing_task_returns_404(
    client: TestClient,
) -> None:
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found",
    }


def test_get_task_rejects_non_integer_id(
    client: TestClient,
) -> None:
    response = client.get("/tasks/not-an-integer")

    assert response.status_code == 422


def test_patch_task_title_only(
    client: TestClient,
) -> None:
    created_task = create_task(
        client,
        "Original title",
    )

    task_id = created_task["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={"title": "Updated title"},
    )

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == task_id
    assert response_body["title"] == "Updated title"
    assert response_body["completed"] is False


def test_patch_task_completed_only(
    client: TestClient,
) -> None:
    created_task = create_task(client)

    task_id = created_task["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={"completed": True},
    )

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["title"] == created_task["title"]
    assert response_body["completed"] is True


def test_patch_task_can_set_completed_back_to_false(
    client: TestClient,
) -> None:
    created_task = create_task(client)

    task_id = created_task["id"]

    client.patch(
        f"/tasks/{task_id}",
        json={"completed": True},
    )

    response = client.patch(
        f"/tasks/{task_id}",
        json={"completed": False},
    )

    assert response.status_code == 200
    assert response.json()["completed"] is False


def test_patch_task_rejects_empty_body(
    client: TestClient,
) -> None:
    created_task = create_task(client)

    response = client.patch(
        f"/tasks/{created_task['id']}",
        json={},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "No fields provided for update",
    }


def test_patch_missing_task_returns_404(
    client: TestClient,
) -> None:
    response = client.patch(
        "/tasks/999999",
        json={"completed": True},
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found",
    }


def test_patch_task_rejects_empty_title(
    client: TestClient,
) -> None:
    created_task = create_task(client)

    response = client.patch(
        f"/tasks/{created_task['id']}",
        json={"title": ""},
    )

    assert response.status_code == 422


def test_patch_task_rejects_null_value(
    client: TestClient,
) -> None:
    created_task = create_task(client)

    response = client.patch(
        f"/tasks/{created_task['id']}",
        json={"title": None},
    )

    assert response.status_code == 422


def test_delete_existing_task(
    client: TestClient,
) -> None:
    created_task = create_task(
        client,
        "Task to delete",
    )

    task_id = created_task["id"]

    delete_response = client.delete(f"/tasks/{task_id}")

    assert delete_response.status_code == 204
    assert delete_response.content == b""

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404


def test_delete_missing_task_returns_404(
    client: TestClient,
) -> None:
    response = client.delete("/tasks/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found",
    }


def test_delete_task_rejects_non_integer_id(
    client: TestClient,
) -> None:
    response = client.delete("/tasks/not-an-integer")

    assert response.status_code == 422
