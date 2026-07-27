def test_list_tasks_empty_returns_empty_array(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_returns_created_tasks(client):
    client.post("/tasks", json={"title": "Task A", "description": ""})
    client.post("/tasks", json={"title": "Task B", "description": ""})

    response = client.get("/tasks")

    assert response.status_code == 200
    titles = [t["title"] for t in response.json()]
    assert titles == ["Task A", "Task B"]
