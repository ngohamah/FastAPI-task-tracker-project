import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.storage import TaskStore


@pytest.fixture
def store():
    fresh_store = TaskStore()
    app.state.store = fresh_store
    yield fresh_store


@pytest.fixture
def client(store):
    return TestClient(app)
