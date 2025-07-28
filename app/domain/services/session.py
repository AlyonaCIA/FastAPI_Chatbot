"""Session service - SOLO business logic."""
import logging
from typing import Optional, Dict

from app.domain.repositories.session import SessionRepositoryInterface

logger = logging.getLogger(__name__)


class SessionService:
    """Handles session business logic."""
    
    def __init__(self, session_repository: SessionRepositoryInterface):
        """Initialize with session repository dependency."""
        self._session_repo = session_repository

    def create_session(self, language: str = "en") -> str:
        """Create a new session with business validation."""
        # Business rule: validate language
        if language not in ["en", "nb"]:
            logger.warning(f"Unsupported language: {language}, defaulting to 'en'")
            language = "en"
        
        # Delegate to repository
        session_id = self._session_repo.create_session(language)
        logger.info(f"Session created: {session_id} with language {language}")
        return session_id

    def get_session(self, session_id: str) -> Optional[Dict]:
        """Get session with validation."""
        if not session_id or not session_id.strip():
            logger.warning("Empty session ID provided")
            return None
        
        return self._session_repo.get_session(session_id)

    def update_session(self, session_id: str, data: Dict) -> bool:
        """Update session with validation."""
        if not data:
            logger.warning("No data provided for session update")
            return False
        
        return self._session_repo.update_session(session_id, data)

    def delete_session(self, session_id: str) -> bool:
        """Delete session."""
        return self._session_repo.delete_session(session_id)

    def add_message_to_history(self, session_id: str, user_message: str, bot_response: str) -> bool:
        """Add message exchange to session history - BUSINESS LOGIC."""
        session = self.get_session(session_id)
        if not session:
            return False
        
        # Business logic: structure the conversation entry
        from datetime import datetime
        message_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_message": user_message,
            "bot_response": bot_response
        }
        
        history = session.get("conversation_history", [])
        history.append(message_entry)
        
        return self.update_session(session_id, {"conversation_history": history})
