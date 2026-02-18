"""Integration test for full conversation flow."""

# ✅ Third-Party Imports
import pytest
from fastapi.testclient import TestClient

# ✅ Local Application Imports
from app.main import app

client = TestClient(app)


def test_full_conversation_flow():
    """Test a complete conversation from start to finish."""

    # 1. Start the conversation
    start_response = client.post("/api/v1/conversations/start", json={"language": "en"})
    assert (
        start_response.status_code == 200
    ), f"Failed to start conversation: {start_response.text}"

    session_data = start_response.json()
    session_id = session_data.get("session_id")

    assert (
        isinstance(session_id, str) and session_id
    ), f"Invalid session_id: {session_id}"

    # 2. Verify welcome message
    welcome_message = session_data.get("message", "")
    assert isinstance(welcome_message, str), "Welcome message should be a string"
    assert len(welcome_message) > 0, "Welcome message should not be empty"

    # 3. Test greeting message
    response = client.post(f"/api/v1/conversations/{session_id}/messages", json={"message": "hello"})
    assert response.status_code == 200, f"Failed to send message: {response.text}"
    assert "message" in response.json(), "Response should contain 'message'"
    
    bot_response = response.json()["message"]
    # Verify it's one of the greeting responses
    greeting_responses = [
        "Hello! I am a chatbot!",
        "Hi there!",
        "Hello! How can I assist you today?",
    ]
    assert bot_response in greeting_responses, f"Unexpected greeting: {bot_response}"

    # 4. Test joke request - chatbot has multiple jokes, any non-fallback response is valid
    response = client.post(f"/api/v1/conversations/{session_id}/messages", json={"message": "Tell me a joke"})
    assert response.status_code == 200, f"Failed to send message: {response.text}"
    assert "message" in response.json(), "Response should contain 'message'"
    
    bot_response = response.json()["message"]
    # Verify it's NOT the fallback message (any joke from dataset is valid)
    assert bot_response != "I'm sorry, I didn't understand that.", \
        "Chatbot should provide a joke, not a fallback message"
    assert len(bot_response) > 0, "Joke response should not be empty"

    # 5. Test unrecognized message - should return fallback
    response = client.post(f"/api/v1/conversations/{session_id}/messages", json={"message": "xyzabc123unknown"})
    assert response.status_code == 200, f"Failed to send message: {response.text}"
    assert "message" in response.json(), "Response should contain 'message'"
    
    bot_response = response.json()["message"]
    # For completely unknown input, expect one of the fallback messages
    fallback_messages = [
        "I'm sorry, I didn't understand that.",
        "Oops, I didn't understand that.",
    ]
    assert bot_response in fallback_messages, \
        f"Expected fallback message for unknown input, got: {bot_response}"

    # 6. Test with expired/non-existent session
    expired_response = client.post(
        "/api/v1/conversations/00000000-0000-0000-0000-000000000000/messages",
        json={"message": "hello"},
    )
    assert expired_response.status_code == 404, "Expected 404 for non-existent session"
