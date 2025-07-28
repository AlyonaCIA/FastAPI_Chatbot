"""Unit tests for SessionManager."""

# ✅ Standard Library Imports
from datetime import datetime
from uuid import UUID

# ✅ Third-Party Imports
import pytest

# ✅ Local Application Imports
from backend.utils.session_manager import SessionManager


@pytest.fixture
def session_manager():
    """Fixture to initialize a new SessionManager instance."""
    return SessionManager()

# ---------------------- #
# TEST SESSION CREATION #
# ---------------------- #


def test_create_session(session_manager):
    """Test creating a new session and verifying its attributes."""
    session_id = session_manager.create_session(language="en")

    # Validate session ID format
    assert isinstance(session_id, str), "Session ID should be a string"
    try:
        UUID(session_id)
    except ValueError:
        pytest.fail(f"Invalid UUID format: {session_id}")

    # Validate session data
    session_data = session_manager.get_session(session_id)
    assert session_data is not None, "Session should exist after creation"
    assert session_data["language"] == "en", "Session language should match"
    assert isinstance(session_data["created_at"],
                      datetime), "Created_at should be a datetime object"


def test_create_multiple_sessions(session_manager):
    """Ensure multiple sessions are created with unique session IDs."""
    session_1 = session_manager.create_session("en")
    session_2 = session_manager.create_session("es")

    assert session_1 != session_2, "Session IDs should be unique"

# ---------------------- #
# TEST SESSION RETRIEVAL #
# ---------------------- #


def test_get_existing_session(session_manager):
    """Test retrieving an existing session."""
    session_id = session_manager.create_session("nb")  # Norwegian language
    session_data = session_manager.get_session(session_id)

    assert session_data is not None, "Session should be retrievable"
    assert session_data["language"] == "nb", "Language should match the assigned value"


def test_get_nonexistent_session(session_manager):
    """Test retrieving a session that does not exist."""
    session_data = session_manager.get_session("invalid-session-id")
    assert session_data is None, "Nonexistent session should return None"

# ---------------------- #
# TEST SESSION UPDATES #
# ---------------------- #


def test_update_existing_session(session_manager):
    """Test updating an existing session with new data."""
    session_id = session_manager.create_session("en")

    update_success = session_manager.update_session(session_id, {"language": "fr"})
    assert update_success, "Session update should return True"

    session_data = session_manager.get_session(session_id)
    assert session_data["language"] == "fr", "Language should be updated to 'fr'"


def test_update_nonexistent_session(session_manager):
    """Test updating a non-existent session."""
    update_success = session_manager.update_session(
        "invalid-session-id", {"language": "de"})
    assert not update_success, "Updating a nonexistent session should return False"

# ---------------------- #
# TEST SESSION DELETION #
# ---------------------- #


def test_delete_existing_session(session_manager):
    """Test deleting an existing session."""
    session_id = session_manager.create_session("es")
    delete_success = session_manager.delete_session(session_id)

    assert delete_success, "Session deletion should return True"
    assert session_manager.get_session(session_id) is None, "Session should be removed"


def test_delete_nonexistent_session(session_manager):
    """Test attempting to delete a session that does not exist."""
    delete_success = session_manager.delete_session("nonexistent-id")
    assert not delete_success, "Deleting a nonexistent session should return False"
