import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.routes.fuelstocks import reset_store


@pytest.fixture
def client() -> TestClient:
    reset_store()
    return TestClient(app)


@pytest.fixture
def diesel_payload() -> dict:
    return {
        "site_id": 1,
        "fuel_type": "diesel",
        "quantity_gallons": 4000,
        "capacity_gallons": 10000,
    }
