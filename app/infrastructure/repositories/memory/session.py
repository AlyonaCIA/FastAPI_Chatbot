"""In-memory session repository implementation."""
# Standard library imports
import logging
from datetime import datetime
from uuid import uuid4
from typing import Dict, Optional


from app.domain.repositories.session import SessionRepositoryInterface

logger = logging.getLogger(__name__)


class InMemorySessionRepository(SessionRepositoryInterface):
    """In-memory implementation of session repository."""
    
    def __init__(self):
        """Initialize with empty sessions dictionary."""
        self._sessions: Dict[str, Dict] = {}
        logger.info("InMemorySessionRepository initialized")

    def create_session(self, language: str = "en") -> str:
        """Create a new session and return session ID."""
        session_id = str(uuid4())
        session_data = {
            "id": session_id,
            "language": language,
            "created_at": datetime.now(),
            "conversation_history": [],
            "last_activity": datetime.now()
        }
        
        self._sessions[session_id] = session_data
        logger.debug(f"Session created: {session_id} with language {language}")
        return session_id

    def get_session(self, session_id: str) -> Optional[Dict]:
        """Get session by ID."""
        session = self._sessions.get(session_id)
        if session:
            # Update last activity
            session["last_activity"] = datetime.now()
            logger.debug(f"Session retrieved: {session_id}")
        else:
            logger.debug(f"Session not found: {session_id}")
        return session

    def update_session(self, session_id: str, data: Dict) -> bool:
        """Update session data."""
        if session_id not in self._sessions:
            logger.warning(f"Cannot update non-existent session: {session_id}")
            return False
        
        self._sessions[session_id].update(data)
        self._sessions[session_id]["last_activity"] = datetime.now()
        logger.debug(f"Session updated: {session_id}")
        return True

    def delete_session(self, session_id: str) -> bool:
        """Delete session."""
        if session_id in self._sessions:
            del self._sessions[session_id]
            logger.debug(f"Session deleted: {session_id}")
            return True
        
        logger.warning(f"Cannot delete non-existent session: {session_id}")
        return False
    
    def get_all_sessions(self) -> Dict[str, Dict]:
        """Get all sessions (for debugging)."""
        logger.debug(f"Retrieved all sessions: {len(self._sessions)} total")
        return self._sessions.copy()
    
    def cleanup_expired_sessions(self, max_age_hours: int = 24) -> int:
        """Remove sessions older than max_age_hours."""
        from datetime import timedelta
        
        cutoff_time = datetime.now() - timedelta(hours=max_age_hours)
        expired_sessions = []
        
        for session_id, session_data in self._sessions.items():
            last_activity = session_data.get("last_activity", session_data.get("created_at"))
            if last_activity < cutoff_time:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            self.delete_session(session_id)
        
        logger.info(f"Cleaned up {len(expired_sessions)} expired sessions")
        return len(expired_sessions)
