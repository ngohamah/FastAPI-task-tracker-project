def test_create_task_returns_201_with_task(client):
    response = client.post(
        "/tasks", json={"title": "Buy milk", "description": "2%, whole aisle"}
    )

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Buy milk"
    assert body["description"] == "2%, whole aisle"
    assert body["status"] == "pending"
    assert "id" in body


def test_create_task_without_title_is_rejected(client):
    response = client.post("/tasks", json={"title": "", "description": "x"})

    assert response.status_code == 422
