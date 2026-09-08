"""FuelStock: the main data object (see docs/project-charter.md, Initial Data Model)."""

from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field, model_validator


class FuelType(str, Enum):
    DIESEL = "diesel"
    GASOLINE = "gasoline"
    JET_A = "jet-a"


class FuelStockCreate(BaseModel):
    """Payload for creating a fuel stock record."""

    site_id: int = Field(ge=1, description="Site that holds this stock")
    fuel_type: FuelType
    quantity_gallons: float = Field(ge=0, description="Gallons currently on hand")
    capacity_gallons: float = Field(gt=0, description="Tank capacity in gallons")

    @model_validator(mode="after")
    def quantity_within_capacity(self) -> "FuelStockCreate":
        if self.quantity_gallons > self.capacity_gallons:
            raise ValueError("quantity_gallons cannot exceed capacity_gallons")
        return self


class FuelStock(FuelStockCreate):
    """A stored fuel stock record."""

    id: int
    last_updated: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="UTC timestamp of the last change",
    )
