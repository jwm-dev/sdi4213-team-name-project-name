"""Health endpoint, used later by Docker, deployment checks and Kubernetes probes."""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
