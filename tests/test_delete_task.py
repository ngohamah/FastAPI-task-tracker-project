def test_delete_task_removes_it(client):
    created = client.post("/tasks", json={"title": "Task A", "description": ""}).json()

    response = client.delete(f"/tasks/{created['id']}")
    assert response.status_code == 204

    follow_up = client.get(f"/tasks/{created['id']}")
    assert follow_up.status_code == 404


def test_delete_task_unknown_id_returns_404(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404
