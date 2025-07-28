"""Session repository interface - Define QUÉ puede hacer."""
# Standard library imports
from abc import ABC, abstractmethod
from typing import Optional, Dict


class SessionRepositoryInterface(ABC):
    """Interface that defines what a session repository must do."""
    
    @abstractmethod
    def create_session(self, language: str = "en") -> str:
        """Create a new session and return session ID."""
        pass
    
    @abstractmethod
    def get_session(self, session_id: str) -> Optional[Dict]:
        """Get session by ID."""
        pass
    
    @abstractmethod
    def update_session(self, session_id: str, data: Dict) -> bool:
        """Update session data."""
        pass
    
    @abstractmethod
    def delete_session(self, session_id: str) -> bool:
        """Delete session."""
        pass
    
    @abstractmethod
    def get_all_sessions(self) -> Dict[str, Dict]:
        """Get all sessions (for debugging)."""
        pass
