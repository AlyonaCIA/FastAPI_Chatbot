"""Session entity - Define la estructura de datos."""

# Standard library imports
from dataclasses import dataclass
from datetime import datetime

# Typing imports (still standard library, but often grouped separately for clarity)
from typing import Any, Dict, List


@dataclass
class SessionData:
    """Session data structure."""

    id: str
    language: str
    created_at: datetime
    conversation_history: List[Dict[str, Any]]

    def add_message(self, user_message: str, bot_response: str) -> None:
        """Add message to conversation history."""
        self.conversation_history.append(
            {
                "timestamp": datetime.now(),
                "user_message": user_message,
                "bot_response": bot_response,
            }
        )
