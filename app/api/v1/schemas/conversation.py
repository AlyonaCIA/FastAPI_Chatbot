"""Conversation API schemas for request/response validation."""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class StartConversationRequest(BaseModel):
    """Request schema for starting a new conversation."""
    language: str = Field(
        default="en", 
        description="Language for the conversation", 
        pattern="^(en|nb)$",
        example="en"
    )


class StartConversationResponse(BaseModel):
    """Response schema for starting a new conversation."""
    session_id: str = Field(description="Unique session identifier")
    message: str = Field(description="Bot greeting message")
    success: bool = Field(description="Operation success indicator")


class MessageRequest(BaseModel):
    """Request schema for sending a message."""
    message: str = Field(
        min_length=1, 
        max_length=1000,
        description="Your message to the chatbot",
        example="Hello, how are you?"
    )


class MessageResponse(BaseModel):
    """Response schema for message replies."""
    session_id: str = Field(description="Session identifier")
    message: str = Field(description="Bot response message")
    confidence: Optional[float] = Field(
        default=None, 
        description="Response confidence score"
    )
    timestamp: Optional[datetime] = Field(
        default=None, 
        description="Response timestamp"
    )
    success: bool = Field(description="Operation success indicator")


class SessionDebugResponse(BaseModel):
    """Response schema for session debugging."""
    total_sessions: int = Field(description="Total number of active sessions")
    session_ids: list[str] = Field(description="List of session IDs")


class ErrorResponse(BaseModel):
    """Error response schema."""
    detail: str = Field(description="Error message")
    error_code: Optional[str] = Field(default=None, description="Error code")
