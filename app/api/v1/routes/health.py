"""Health check API routes."""
# Standard library imports
from datetime import datetime

# Third-party imports
from fastapi import APIRouter

# Local application imports
from app.api.v1.schemas.common import HealthResponse


router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="1.0.1"
    )
