"""Module to create a ssession."""
# backend/utils/session_manager.py

# ✅ Standard Library Imports
import logging
from datetime import datetime
from typing import Dict, Optional
from uuid import uuid4

logger = logging.getLogger(__name__)


class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, dict] = {}

    def create_session(self, language: str = "en") -> str:
        session_id = str(uuid4())
        self.sessions[session_id] = {
            "created_at": datetime.now(),
            "language": language,
            "conversation_history": []
        }
        logger.debug(f"New session created: {session_id} with language {language}")
        return session_id

    def get_session(self, session_id: str) -> Optional[dict]:
        session = self.sessions.get(session_id)
        if not session:
            logger.debug(f"Session not found: {session_id}")
        return session

    def update_session(self, session_id: str, data: dict) -> bool:
        if session_id in self.sessions:
            self.sessions[session_id].update(data)
            return True
        return False

    def delete_session(self, session_id: str) -> bool:
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False
