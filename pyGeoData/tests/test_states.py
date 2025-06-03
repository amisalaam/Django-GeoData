import pytest
from fastapi.testclient import TestClient
from pyGeoData.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_state(client):
    response = client.post("/v1/states/", json={"name": "Test State", "country_id": 1})
    assert response.status_code == 200
    assert response.json()["name"] == "Test State"

def test_read_states(client):
    response = client.get("/v1/states/")
    assert response.status_code == 200
    assert len(response.json()) >= 2  # At least 2 states from sample data
