import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.routes.fuelstocks import reset_store

LEVEL_MARKERS = {"l0", "l1", "l2"}


def pytest_collection_modifyitems(items):
    """Every test carries exactly one level marker; unmarked tests are L0."""
    for item in items:
        if not LEVEL_MARKERS & {m.name for m in item.iter_markers()}:
            item.add_marker(pytest.mark.l0)


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
