def test_filter_tasks_by_status(client):
    a = client.post("/tasks", json={"title": "Task A", "description": ""}).json()
    client.post("/tasks", json={"title": "Task B", "description": ""})
    client.patch(f"/tasks/{a['id']}", json={"status": "done"})

    response = client.get("/tasks", params={"status": "done"})

    assert response.status_code == 200
    titles = [t["title"] for t in response.json()]
    assert titles == ["Task A"]


def test_filter_tasks_by_pending_status(client):
    client.post("/tasks", json={"title": "Task A", "description": ""})

    response = client.get("/tasks", params={"status": "pending"})

    assert response.status_code == 200
    assert len(response.json()) == 1
