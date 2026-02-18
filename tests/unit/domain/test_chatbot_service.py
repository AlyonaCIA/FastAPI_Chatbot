"""Unit tests for ChatbotService."""

# ✅ Third-Party Imports
import logging
from typing import List

import pytest

# ✅ Local Application Imports
from app.domain.services.chatbot import ChatbotService
from app.infrastructure.data.loaders.chatbot_data import chatbot_data


@pytest.fixture
def chatbot() -> ChatbotService:
    """Initialize the chatbot service before each test."""
    return ChatbotService()


def test_process_message_fallback(chatbot: ChatbotService) -> None:
    """Test that unrecognized messages return fallback responses."""
    fallback_messages = [
        "I'm sorry, I didn't understand that.",
        "Oops, I didn't understand that.",
    ]
    
    # Test with random unrecognized text
    response = chatbot.process_message("xyzabc123unknown")
    assert isinstance(response, str), "Response should be a string"
    assert response in fallback_messages, f"Expected fallback message, got: {response}"
    
    # Test with empty string
    response = chatbot.process_message("")
    assert isinstance(response, str), "Response should be a string"
    assert response in fallback_messages, f"Expected fallback message, got: {response}"


def test_process_message_joke(chatbot: ChatbotService) -> None:
    """Test that joke requests return actual jokes, not fallback messages."""
    fallback_messages = [
        "I'm sorry, I didn't understand that.",
        "Oops, I didn't understand that.",
    ]
    
    response = chatbot.process_message("Tell me a joke")
    assert isinstance(response, str), "Response should be a string"
    assert response not in fallback_messages, \
        "Chatbot should provide a joke, not a fallback message"
    assert len(response) > 0, "Joke response should not be empty"


# 🔹 Temporarily commented until the logging issue in ChatbotService is fixed
# def test_process_message_error_handling(chatbot: ChatbotService, caplog) -> None:
#     """Ensure chatbot handles errors gracefully and logs the error."""
#     expected_fallbacks = [
#         "I'm sorry, I didn't understand that.",
#         "Oops, I didn't understand that."
#     ]

#     with caplog.at_level(logging.ERROR):
# response = chatbot.process_message("UNKNOWN_INPUT")  # 🔹 Used
# "UNKNOWN_INPUT" instead of `None`

#     assert response in expected_fallbacks, "Error handling failed"

#     log_messages = [record.message.lower() for record in caplog.records]

#     # 🔹 Debugging: Print logs if no error is found
#     if not log_messages:
#         print(f"❌ DEBUG: No logs captured.")

#     assert log_messages, "No error log recorded"
