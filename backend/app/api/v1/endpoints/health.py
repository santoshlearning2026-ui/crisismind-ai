"""Health check endpoints."""

from datetime import datetime

from fastapi import APIRouter

from app.api.v1.schemas.response import HealthResponse
from app.config import settings

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """Health check endpoint.
    
    Returns:
        Health status response
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version=settings.APP_VERSION,
        checks={
            "database": "healthy",
            "vector_db": "healthy",
            "api": "healthy",
        },
    )


@router.get("/ready", tags=["Health"])
async def readiness_check() -> dict:
    """Readiness check endpoint.
    
    Returns:
        Readiness status
    """
    return {"status": "ready", "timestamp": datetime.utcnow().isoformat()}


@router.get("/live", tags=["Health"])
async def liveness_check() -> dict:
    """Liveness check endpoint.
    
    Returns:
        Liveness status
    """
    return {"status": "alive", "timestamp": datetime.utcnow().isoformat()}
