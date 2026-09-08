"""L2: the API over real HTTP. Run with `pytest -m l2`.

These tests do not assume an empty store (the target may be a long-running
instance), so they only assert on records they created themselves.
"""

import pytest

pytestmark = pytest.mark.l2


def test_health_over_http(http):
    r = http.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
    assert r.headers["content-type"].startswith("application/json")


def test_openapi_docs_are_served(http):
    assert http.get("/docs").status_code == 200
    schema = http.get("/openapi.json").json()
    assert "/fuelstocks" in schema["paths"]
    assert "/health" in schema["paths"]


def test_create_then_get_over_http(http):
    payload = {"site_id": 7, "fuel_type": "gasoline", "quantity_gallons": 250, "capacity_gallons": 1000}
    created = http.post("/fuelstocks", json=payload)
    assert created.status_code == 201
    body = created.json()
    assert body["site_id"] == 7 and body["fuel_type"] == "gasoline"

    fetched = http.get(f"/fuelstocks/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == body

    ids = [item["id"] for item in http.get("/fuelstocks").json()]
    assert body["id"] in ids


def test_unknown_id_is_404_over_http(http):
    r = http.get("/fuelstocks/999999")
    assert r.status_code == 404
    assert "not found" in r.json()["detail"]


def test_validation_error_is_422_over_http(http):
    payload = {"site_id": 1, "fuel_type": "diesel", "quantity_gallons": 5, "capacity_gallons": 1}
    r = http.post("/fuelstocks", json=payload)
    assert r.status_code == 422
    assert "capacity" in r.text
