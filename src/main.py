"""Application entry point.

Run locally:  uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
Docs:         http://localhost:8000/docs
"""

from fastapi import FastAPI

from src.routes import fuelstocks, health

app = FastAPI(
    title="Fuel Inventory Management System",
    description="Tracks fuel stock records across company sites. Team #4 'name', SDI 4213/5213.",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(fuelstocks.router)


@app.get("/", include_in_schema=False)
def root() -> dict[str, str]:
    return {"message": "Fuel Inventory Management System API. See /docs."}
