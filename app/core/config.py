"""Application configuration."""
# Standard library imports
import os
from typing import List

# Third-party imports
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Application
    APP_NAME: str = "FastAPI Chatbot"
    APP_VERSION: str = "1.0.1"
    DEBUG: bool = False
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Chatbot
    DEFAULT_LANGUAGE: str = "en"
    CONFIDENCE_THRESHOLD: float = 0.3
    
    # Session Management
    SESSION_TTL_HOURS: int = 24
    MAX_SESSIONS: int = 1000
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    ALLOWED_METHODS: List[str] = ["GET", "POST"]
    ALLOWED_HEADERS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
