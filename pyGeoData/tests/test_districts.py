import pytest
from fastapi.testclient import TestClient
from pyGeoData.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_district(client):
    response = client.post("/v1/districts/", json={"name": "Test District", "state_id": 1})
    assert response.status_code == 200
    assert response.json()["name"] == "Test District"

def test_read_districts(client):
    response = client.get("/v1/districts/")
    assert response.status_code == 200
    assert len(response.json()) >= 2  # At least 2 districts from sample data
