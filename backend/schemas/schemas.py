# -----------------------------------------------------------------------------
# Why Use a General Schema (`ChatbotData`)?
# -----------------------------------------------------------------------------
# A general schema provides structure and validation for the chatbot's data.
# Instead of dealing with raw JSON dictionaries, a well-defined schema allows:
#
# ✅ **Consistency**: Ensures that all chatbot data follows a uniform structure.
# ✅ **Validation**: Automatically verifies that all fields exist and have the correct types.
# ✅ **Autocompletion & Type Hints**: Improves development experience by providing
#    clear definitions for chatbot responses.
# ✅ **Data Integrity**: Prevents issues caused by missing or incorrectly formatted data.
# ✅ **Documentation**: FastAPI automatically generates documentation when schemas are used.
#
# -----------------------------------------------------------------------------
# When is a General Schema Needed?
# -----------------------------------------------------------------------------
# - If the chatbot JSON structure frequently changes, a schema prevents breaking changes.
# - If the chatbot data is complex (nested structures, optional fields, etc.).
# - If API consumers need consistent responses with predictable fields.
#
# -----------------------------------------------------------------------------
# When is a General Schema NOT Needed?
# -----------------------------------------------------------------------------
# - If the JSON is static and does not require validation.
# - If performance is a primary concern (loading raw JSON is faster than validation).
# - If the application does not require strong type enforcement.
#
# -----------------------------------------------------------------------------
# Implementation of a General Schema
# -----------------------------------------------------------------------------
# The `ChatbotData` schema (defined in `schemas.py`) encapsulates all chatbot-related
# data structures. It includes:
#
# - `Greeting`: Defines greeting messages per language.
# - `Fallback`: Contains default responses when no match is found.
# - `Dialogue`: Manages structured conversations based on keywords.
# - `ReplySet`: Ensures multilingual support for chatbot responses.
#
# This schema is used when loading `kindly-bot.json` in `services.py` and
# throughout the chatbot logic, improving maintainability and type safety.
#
# -----------------------------------------------------------------------------
# Example Usage in `main.py`
# -----------------------------------------------------------------------------
# The following implementation utilizes `ChatbotData` to process chatbot
# conversations while enforcing structured responses.
# Example
# -----------------------------------------------------------------------------
"""General Schema for Chatbot Data This schema defines the structure of the chatbot JSON
data, ensuring consistency when loading and processing it.

# Import required libraries
from pydantic import BaseModel
from typing import List, Dict, Optional


Defines a set of replies in different languages.
Each language key contains a list of possible responses.

class ReplySet(BaseModel):
    en: List[str]  # English responses
    nb: List[str]  # Norwegian responses


Defines the schema for chatbot greetings.
Each greeting has an ID and a set of multilingual replies.

class Greeting(BaseModel):
    id: str  # Unique identifier for the greeting
    replies: ReplySet  # Associated replies


Defines the schema for chatbot fallback responses.
Fallbacks are used when the chatbot doesn't recognize user input.

class Fallback(BaseModel):
    id: str  # Unique identifier for the fallback message
    replies: ReplySet  # Associated replies


Defines the structure of a chatbot dialogue entry.
Each dialogue entry has an ID, a type, optional parent ID, keywords, samples, and replies.

class Dialogue(BaseModel):
    id: str  # Unique identifier for the dialogue
    dialogue_type: str  # Type of dialogue (e.g., greeting, question, statement)
    parent_id: Optional[str] = None  # Optional reference to a parent dialogue
    keywords: Optional[Dict[str, List[str]]] = {}  # Keywords associated with the dialogue
    samples: Optional[Dict[str, List[str]]] = {}  # Example user messages triggering this dialogue
    replies: ReplySet  # Possible replies in different languages


Defines the overall chatbot dataset structure.
It contains lists of greetings, fallbacks, and dialogues.

class ChatbotData(BaseModel):
    greetings: List[Greeting]  # List of chatbot greeting messages
    fallbacks: List[Fallback]  # List of fallback responses
    dialogues: List[Dialogue]  # List of dialogue entries
"""
# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# ✅ The chatbot follows a structured approach using `ChatbotData`.
# ✅ User conversations are tracked, and language preferences are respected.
# ✅ Responses are dynamically selected based on predefined dialogues.
# ✅ The implementation ensures robustness and maintainability.
#
# If performance optimization is needed, consider loading raw JSON data
# directly instead of enforcing schema validation.
#
# -----------------------------------------------------------------------------
