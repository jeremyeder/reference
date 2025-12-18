"""Health check endpoints for Kubernetes and monitoring."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """
    Basic health check endpoint.

    Returns:
        Health status
    """
    return {"status": "healthy"}


@router.get("/readiness")
def readiness_check() -> dict[str, str]:
    """
    Kubernetes readiness probe endpoint.

    Returns:
        Readiness status
    """
    return {"status": "ready"}


@router.get("/liveness")
def liveness_check() -> dict[str, str]:
    """
    Kubernetes liveness probe endpoint.

    Returns:
        Liveness status
    """
    return {"status": "alive"}
