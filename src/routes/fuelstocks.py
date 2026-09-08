"""Fuel stock endpoints.

Week 3 skeleton: an in-memory store so the API is runnable and testable now.
It is replaced by SQLite/SQLAlchemy in a later milestone without changing the
HTTP contract.
"""

from fastapi import APIRouter, HTTPException, status

from src.models.fuelstock import FuelStock, FuelStockCreate

router = APIRouter(prefix="/fuelstocks", tags=["fuelstocks"])

_store: dict[int, FuelStock] = {}
_next_id = 1


def reset_store() -> None:
    """Clear all records; used by the test suite."""
    global _next_id
    _store.clear()
    _next_id = 1


@router.get("", response_model=list[FuelStock])
def list_fuelstocks() -> list[FuelStock]:
    return list(_store.values())


@router.post("", response_model=FuelStock, status_code=status.HTTP_201_CREATED)
def create_fuelstock(payload: FuelStockCreate) -> FuelStock:
    global _next_id
    record = FuelStock(id=_next_id, **payload.model_dump())
    _store[record.id] = record
    _next_id += 1
    return record


@router.get("/{stock_id}", response_model=FuelStock)
def get_fuelstock(stock_id: int) -> FuelStock:
    record = _store.get(stock_id)
    if record is None:
        raise HTTPException(status_code=404, detail=f"fuel stock {stock_id} not found")
    return record
