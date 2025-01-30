"""Module main for FastAPI Chatbot."""

# ✅ Standard Library Imports
import logging
from typing import Dict

# ✅ Third-Party Imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ✅ Local Application Imports
from backend.services.chatbot_service import ChatbotService
from backend.utils.session_manager import SessionManager

# ✅ Initialization
session_manager = SessionManager()
chatbot_service = ChatbotService()

# Configuration logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Chatbot API 🤖💬",
    version="1.0.0",
    description="""
    ## 🚀 How to Use the API:

    1️⃣ **Start a conversation** using `/api/conversation/start`
    2️⃣ **Use the received `session_id`** to send messages via `/api/conversation/message`

    ### 🔹 Example:
    ```python
    # 1️⃣ Start a conversation
    POST /api/conversation/start?language=en
    Response: {
        "session_id": "c1091cdd-0d71-4645-9579-ce171f7393d5",
        "message": "Hello! 👋",
        "success": true
    }

    # 2️⃣ Send a message using the session_id
    POST /api/conversation/message?user_id=c1091cdd-0d71-4645-9579-ce171f7393d5&message=Hello
    Response: {
        "message": "Hi there! 😊",
        "success": true
    }
    ```

    ✅ **Features:**
    - Supports multiple languages 🌍 (English, Norwegian, etc.)
    - Keeps track of conversation history 📜
    - Uses NLP to provide smart responses 🤖✨
    """,
)


# Users in memory
users: Dict[str, Dict] = {}


class StartResponse(BaseModel):
    session_id: str
    message: str
    success: bool


class MessageResponse(BaseModel):
    session_id: str
    message: str
    success: bool


@app.post("/api/conversation/start")
@app.post("/api/conversation/start")
async def start_conversation(language: str = "en"):
    """Start a new chatbot conversation and return a greeting."""
    session_id = session_manager.create_session(language)
    # ✅ it is create and save it.
    greeting = chatbot_service.get_greeting(language)

    return {
        "session_id": session_id,
        "message": greeting,
        "success": True
    }


@app.post("/api/conversation/message")
async def process_message(user_id: str, message: str):
    """Process user messages and return a chatbot response."""
    session = session_manager.get_session(user_id)
    if not session:
        logging.warning(f"⚠️ Session not found: {user_id}")
        raise HTTPException(
            status_code=404,
            detail="Session not found. Please start a new conversation."
        )

    response = chatbot_service.process_message(message)

    return {
        "session_id": user_id,
        "message": response,
        "success": True
    }


@app.get("/api/debug/sessions")
async def debug_sessions():
    """Devuelve las sesiones activas en memoria (para depuración)."""
    return {"active_sessions": list(users.keys())}
