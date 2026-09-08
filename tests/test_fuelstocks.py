def test_list_is_empty_initially(client):
    response = client.get("/fuelstocks")
    assert response.status_code == 200
    assert response.json() == []


def test_create_then_get_fuelstock(client, diesel_payload):
    created = client.post("/fuelstocks", json=diesel_payload)
    assert created.status_code == 201
    body = created.json()
    assert body["id"] == 1
    assert body["fuel_type"] == "diesel"
    assert body["quantity_gallons"] == 4000
    assert "last_updated" in body

    fetched = client.get("/fuelstocks/1")
    assert fetched.status_code == 200
    assert fetched.json() == body

    listed = client.get("/fuelstocks")
    assert [item["id"] for item in listed.json()] == [1]


def test_get_unknown_id_returns_404(client):
    response = client.get("/fuelstocks/999")
    assert response.status_code == 404


def test_quantity_cannot_exceed_capacity(client, diesel_payload):
    diesel_payload["quantity_gallons"] = 12000  # capacity is 10000
    response = client.post("/fuelstocks", json=diesel_payload)
    assert response.status_code == 422
    assert "capacity" in response.text


def test_unknown_fuel_type_is_rejected(client, diesel_payload):
    diesel_payload["fuel_type"] = "kerosene"
    response = client.post("/fuelstocks", json=diesel_payload)
    assert response.status_code == 422
