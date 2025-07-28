"""Conversation API routes."""
# Standard library imports
import logging

# Third-party imports
from fastapi import APIRouter, HTTPException, Depends

# Local application imports
from app.api.dependencies import get_chatbot_service, get_session_service
from app.api.v1.schemas.conversation import (
    StartConversationRequest,
    StartConversationResponse,
    MessageRequest,
    MessageResponse,
    SessionDebugResponse,
)
from app.domain.services.chatbot import ChatbotService
from app.domain.services.session import SessionService


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.post("/start", response_model=StartConversationResponse)
async def start_conversation(
    request: StartConversationRequest = StartConversationRequest(),
    chatbot_service: ChatbotService = Depends(get_chatbot_service),
    session_service: SessionService = Depends(get_session_service)
):
    """Start a new conversation."""
    try:
        logger.info(f"Starting conversation with language: {request.language}")
        
        # Create session
        session_id = session_service.create_session(request.language)
        logger.info(f"Created session_id: {session_id}")
        
        # Verify session was created
        verify_session = session_service.get_session(session_id)
        logger.info(f"Session verification: {verify_session is not None}")
        
        # Get greeting
        greeting = chatbot_service.get_greeting(request.language)
        logger.info(f"Generated greeting: {greeting}")
        
        return StartConversationResponse(
            session_id=session_id,
            message=greeting,
            success=True
        )
        
    except Exception as e:
        logger.error(f"Error starting conversation: {e}")
        raise HTTPException(status_code=500, detail="Failed to start conversation")


@router.post("/{session_id}/messages", response_model=MessageResponse)
async def send_message(
    session_id: str,
    request: MessageRequest,
    chatbot_service: ChatbotService = Depends(get_chatbot_service),
    session_service: SessionService = Depends(get_session_service)
):
    """Send a message in a conversation."""
    try:
        logger.info(f"Processing message for session_id: '{session_id}'")
        logger.info(f"Session_id type: {type(session_id)}")
        logger.info(f"Session_id length: {len(session_id)}")
        logger.info(f"Message content: '{request.message}'")
        
        # Debug: Get all sessions
        all_sessions = session_service._session_repo.get_all_sessions()
        logger.info(f"Total sessions in memory: {len(all_sessions)}")
        logger.info(f"Available session_ids: {list(all_sessions.keys())}")
        
        # Verify session exists
        session = session_service.get_session(session_id)
        logger.info(f"Session found: {session is not None}")
        
        if not session:
            logger.error(f"Session '{session_id}' not found!")
            logger.error(f"Available sessions: {list(all_sessions.keys())}")
            raise HTTPException(
                status_code=404,
                detail=f"Session '{session_id}' not found. Available sessions: {len(all_sessions)}"
            )
        
        logger.info(f"Session data: {session}")
        
        # Process message
        bot_response = chatbot_service.process_message(request.message)
        logger.info(f"Bot response: {bot_response}")
        
        # Add to conversation history
        history_updated = session_service.add_message_to_history(
            session_id, 
            request.message, 
            bot_response
        )
        logger.info(f"History updated: {history_updated}")
        
        return MessageResponse(
            session_id=session_id,
            message=bot_response,
            success=True
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process message: {str(e)}")


@router.get("/debug/sessions", response_model=SessionDebugResponse)
async def debug_sessions(
    session_service: SessionService = Depends(get_session_service)
):
    """Get debug information about active sessions."""
    try:
        sessions = session_service._session_repo.get_all_sessions()
        logger.info(f"Debug: Found {len(sessions)} sessions")
        
        return SessionDebugResponse(
            total_sessions=len(sessions),
            session_ids=list(sessions.keys())
        )
        
    except Exception as e:
        logger.error(f"Error getting debug info: {e}")
        raise HTTPException(status_code=500, detail="Failed to get debug info")
