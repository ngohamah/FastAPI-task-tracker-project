import logging

from fastapi.testclient import TestClient

from app import storage
from app.main import app


def test_request_logging_emits_log_line(client, caplog):
    with caplog.at_level(logging.INFO, logger="task_tracker"):
        client.get("/health")

    assert any("GET /health -> 200" in record.message for record in caplog.records)


def test_unhandled_exception_is_logged_and_returns_500(caplog, monkeypatch):
    def boom(*args, **kwargs):
        raise RuntimeError("storage exploded")

    monkeypatch.setattr(storage.store, "list", boom)
    no_raise_client = TestClient(app, raise_server_exceptions=False)

    with caplog.at_level(logging.ERROR, logger="task_tracker"):
        response = no_raise_client.get("/tasks")

    assert response.status_code == 500
    assert any("Unhandled error" in record.message for record in caplog.records)
