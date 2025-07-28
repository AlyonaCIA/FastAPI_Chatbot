"""Custom exceptions for the application."""


class ChatbotException(Exception):
    """Base exception for chatbot errors."""
    pass


class SessionNotFoundException(ChatbotException):
    """Raised when session is not found."""
    pass


class InvalidLanguageException(ChatbotException):
    """Raised when unsupported language is requested."""
    pass


class DataLoadingException(ChatbotException):
    """Raised when chatbot data cannot be loaded."""
    pass


class MessageProcessingException(ChatbotException):
    """Raised when message processing fails."""
    pass
