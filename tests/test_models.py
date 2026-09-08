"""Unit tests for the FuelStock model: no HTTP, no app, just validation rules."""

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from src.models.fuelstock import FuelStock, FuelStockCreate, FuelType


def test_fuel_type_values_match_charter():
    assert {t.value for t in FuelType} == {"diesel", "gasoline", "jet-a"}


def test_valid_payload_is_accepted():
    stock = FuelStockCreate(site_id=3, fuel_type="jet-a", quantity_gallons=0, capacity_gallons=500)
    assert stock.fuel_type is FuelType.JET_A
    assert stock.quantity_gallons == 0


def test_quantity_equal_to_capacity_is_allowed():
    stock = FuelStockCreate(site_id=1, fuel_type="diesel", quantity_gallons=100, capacity_gallons=100)
    assert stock.quantity_gallons == stock.capacity_gallons


def test_quantity_above_capacity_is_rejected():
    with pytest.raises(ValidationError, match="cannot exceed capacity"):
        FuelStockCreate(site_id=1, fuel_type="diesel", quantity_gallons=101, capacity_gallons=100)


@pytest.mark.parametrize(
    "field, value",
    [
        ("site_id", 0),
        ("quantity_gallons", -1),
        ("capacity_gallons", 0),
        ("fuel_type", "kerosene"),
    ],
)
def test_out_of_range_fields_are_rejected(field, value):
    payload = {"site_id": 1, "fuel_type": "gasoline", "quantity_gallons": 10, "capacity_gallons": 20}
    payload[field] = value
    with pytest.raises(ValidationError):
        FuelStockCreate(**payload)


def test_fuelstock_defaults_last_updated_to_utc_now():
    before = datetime.now(timezone.utc)
    stock = FuelStock(id=1, site_id=1, fuel_type="diesel", quantity_gallons=1, capacity_gallons=2)
    assert stock.last_updated.tzinfo is not None
    assert before <= stock.last_updated <= datetime.now(timezone.utc)
