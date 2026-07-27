def test_update_task_partial_fields(client):
    created = client.post("/tasks", json={"title": "Task A", "description": "orig"}).json()

    response = client.patch(f"/tasks/{created['id']}", json={"status": "done"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "done"
    assert body["title"] == "Task A"
    assert body["description"] == "orig"


def test_update_task_unknown_id_returns_404(client):
    response = client.patch("/tasks/999", json={"status": "done"})

    assert response.status_code == 404
