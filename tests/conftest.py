import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.storage import store


@pytest.fixture(autouse=True)
def reset_store():
    store._tasks.clear()
    store._next_id = 1
    yield


@pytest.fixture
def client():
    return TestClient(app)
