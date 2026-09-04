def test_list_tasks_with_invalid_status_is_rejected(client):
    response = client.get("/tasks", params={"status": "not-a-real-status"})

    assert response.status_code == 422


def test_patch_can_clear_description_to_empty_string(client):
    created = client.post("/tasks", json={"title": "Task A", "description": "orig"}).json()

    response = client.patch(f"/tasks/{created['id']}", json={"description": ""})

    assert response.status_code == 200
    assert response.json()["description"] == ""


def test_create_task_with_title_over_max_length_is_rejected(client):
    response = client.post("/tasks", json={"title": "x" * 201, "description": ""})

    assert response.status_code == 422


def test_create_task_with_title_at_max_length_is_accepted(client):
    response = client.post("/tasks", json={"title": "x" * 200, "description": ""})

    assert response.status_code == 201


def test_update_task_with_title_over_max_length_is_rejected(client):
    created = client.post("/tasks", json={"title": "Task A", "description": ""}).json()

    response = client.patch(f"/tasks/{created['id']}", json={"title": "x" * 201})

    assert response.status_code == 422


def test_list_tasks_preserves_creation_order_after_updates_and_deletes(client):
    a = client.post("/tasks", json={"title": "Task A", "description": ""}).json()
    b = client.post("/tasks", json={"title": "Task B", "description": ""}).json()
    c = client.post("/tasks", json={"title": "Task C", "description": ""}).json()

    client.patch(f"/tasks/{b['id']}", json={"status": "done"})

    response = client.get("/tasks")

    ids = [t["id"] for t in response.json()]
    assert ids == [a["id"], b["id"], c["id"]]
