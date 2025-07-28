"""Dependency injection setup for FastAPI."""
# Third-party imports
from fastapi import Depends

# Local application imports
from app.domain.repositories.session import SessionRepositoryInterface
from app.domain.services.chatbot import ChatbotService
from app.domain.services.session import SessionService
from app.infrastructure.repositories.memory.session import InMemorySessionRepository


_session_repository_instance = None
_chatbot_service_instance = None


def get_session_repository() -> SessionRepositoryInterface:
    """Get session repository instance (SINGLETON)."""
    global _session_repository_instance
    if _session_repository_instance is None:
        _session_repository_instance = InMemorySessionRepository()
    return _session_repository_instance


def get_chatbot_service() -> ChatbotService:
    """Get chatbot service instance (SINGLETON)."""
    global _chatbot_service_instance
    if _chatbot_service_instance is None:
        _chatbot_service_instance = ChatbotService()
    return _chatbot_service_instance


def get_session_service(
    repo: SessionRepositoryInterface = Depends(get_session_repository)
) -> SessionService:
    """Get session service with injected repository."""
    return SessionService(repo)
