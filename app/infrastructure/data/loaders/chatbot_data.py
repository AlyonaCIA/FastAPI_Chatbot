"""Module to load chatbot data with proper error handling."""

# Standard library imports
import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)


class ChatbotDataLoader:
    """Handles loading and validation of chatbot training data."""

    @staticmethod
    def load_chatbot_data() -> Dict[str, Any]:
        """Load chatbot data from JSON file with fallback."""
        try:
            # Correct path: infrastructure/data/loaders/../datasets/chatbot-data.json
            data_file = Path(__file__).parent.parent / "datasets" / "chatbot-data.json"

            if not data_file.exists():
                logger.error(f"Chatbot data file not found: {data_file}")
                return ChatbotDataLoader._get_fallback_data()

            logger.info(f"Loading chatbot data from: {data_file}")

            with open(data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Validate data structure
            if not ChatbotDataLoader._validate_data_structure(data):
                logger.error("Invalid data structure, using fallback")
                return ChatbotDataLoader._get_fallback_data()

            logger.info(
                f"Successfully loaded chatbot data with {len(data.get('dialogues', []))} dialogues"
            )
            return data

        except FileNotFoundError as e:
            logger.error(f"Chatbot data file not found: {e}")
            return ChatbotDataLoader._get_fallback_data()

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in chatbot data file: {e}")
            return ChatbotDataLoader._get_fallback_data()

        except Exception as e:
            logger.error(f"Unexpected error loading chatbot data: {e}")
            return ChatbotDataLoader._get_fallback_data()

    @staticmethod
    def _validate_data_structure(data: Dict[str, Any]) -> bool:
        """Validate that loaded data has expected structure."""
        required_keys = ["greetings", "fallbacks", "dialogues"]

        for key in required_keys:
            if key not in data:
                logger.error(f"Missing required key in chatbot data: {key}")
                return False

            if not isinstance(data[key], list):
                logger.error(f"Key '{key}' should be a list, got {type(data[key])}")
                return False

        return True

    @staticmethod
    def _get_fallback_data() -> Dict[str, Any]:
        """Return minimal fallback data if main data can't be loaded."""
        logger.warning("Using fallback chatbot data")
        return {
            "greetings": [
                {
                    "id": "fallback-greeting",
                    "replies": {
                        "en": ["Hello! I am a chatbot."],
                        "nb": ["Hallo! Jeg er en chatbot!"],
                    },
                }
            ],
            "fallbacks": [
                {
                    "id": "fallback-response",
                    "replies": {
                        "en": ["I'm sorry, I didn't understand that."],
                        "nb": ["Beklager, jeg forstod ikke det."],
                    },
                }
            ],
            "dialogues": [],
        }


# Load data on module import (singleton pattern)
chatbot_data = ChatbotDataLoader.load_chatbot_data()
