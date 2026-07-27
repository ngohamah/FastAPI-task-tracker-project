def test_get_task_by_id_returns_task(client):
    created = client.post("/tasks", json={"title": "Task A", "description": ""}).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_get_task_by_unknown_id_returns_404(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
