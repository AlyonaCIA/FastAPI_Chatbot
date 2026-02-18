"""Common schemas shared across API endpoints."""

from typing import Optional

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response schema."""

    status: str = Field(description="Service status")
    timestamp: str = Field(description="Check timestamp")
    version: Optional[str] = Field(default=None, description="API version")


class BaseResponse(BaseModel):
    """Base response schema with common fields."""

    success: bool = Field(description="Operation success indicator")
    message: Optional[str] = Field(default=None, description="Optional message")
