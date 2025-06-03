import pytest
from fastapi.testclient import TestClient
from pyGeoData.main import app
from pyGeoData.core.data_manager import DataManager

@pytest.fixture
def client():
    return TestClient(app)

def test_create_country(client):
    response = client.post("/v1/countries/", json={"name": "Test Country", "code": "TST"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Country"

def test_read_countries(client):
    response = client.get("/v1/countries/")
    assert response.status_code == 200
    assert len(response.json()) >= 2  # At least 2 countries from sample data
