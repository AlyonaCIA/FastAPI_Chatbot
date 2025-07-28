"""Chatbot service with business logic."""
# Standard library imports
import logging
import random
from typing import List, Tuple

# Third-party imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Local application imports
from app.infrastructure.data.loaders.chatbot_data import chatbot_data


logger = logging.getLogger(__name__)


class ChatbotService:
    """Handles chatbot logic and response generation using NLP."""

    def __init__(self):
        """Initialize the chatbot with TF-IDF vectorization and load training data."""
        self.language = "en"
        self.questions, self.answers = self._load_data()

        if not self.questions:
            logger.warning("No training data found. Using basic responses.")
            return

        # Configure TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(
            min_df=1,
            strip_accents='unicode',
            lowercase=True,
            ngram_range=(1, 2)
        )
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

        logger.info(f"ChatbotService initialized with {len(self.questions)} QA pairs.")

    def _load_data(self) -> Tuple[List[str], List[str]]:
        """Extract questions and answers from chatbot_data."""
        questions, answers = [], []

        try:
            for dialogue in chatbot_data.get("dialogues", []):
                samples = dialogue.get("samples", {}).get(self.language, [])
                replies = dialogue.get("replies", {}).get(self.language, [])

                if not replies:
                    logger.warning(f"No replies found for dialogue ID: {dialogue.get('id', 'unknown')}")
                    continue

                for sample in samples:
                    if not isinstance(sample, str) or not sample.strip():
                        continue
                    questions.append(sample.lower().strip())
                    answers.append(random.choice(replies))  # ← Random reply

            logger.info(f"Successfully loaded {len(questions)} questions and {len(answers)} answers.")
            return questions, answers

        except Exception as e:
            logger.error(f"Error loading chatbot data: {str(e)}")
            return [], []

    def process_message(self, user_message: str) -> str:
        """Find the most relevant response using NLP similarity matching."""
        if not user_message or not user_message.strip():
            return self._get_fallback_response()

        # Check for common greetings first
        greeting_response = self._check_for_greeting(user_message)
        if greeting_response:
            return greeting_response

        # If no training data, return fallback
        if not self.questions:
            return self._get_fallback_response()

        try:
            user_message = user_message.lower().strip()
            logger.debug(f"Processing user message: '{user_message}'")

            user_vector = self.vectorizer.transform([user_message])
            similarities = cosine_similarity(user_vector, self.question_vectors).flatten()

            best_match_idx = similarities.argmax()
            confidence = similarities[best_match_idx]

            logger.debug(f"Best match confidence: {confidence:.4f}")

            if confidence < 0.2:  # ← Reduced threshold
                logger.info(f"Low confidence ({confidence:.2f}) for message: '{user_message}'")
                return self._get_fallback_response()

            matched_question = self.questions[best_match_idx]
            logger.info(f"Matched '{user_message}' to '{matched_question}' with confidence {confidence:.2f}")

            return self.answers[best_match_idx]

        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            return self._get_fallback_response()

    def _check_for_greeting(self, user_message: str) -> str:
        """Check if message is a greeting and respond appropriately."""
        greetings = ["hello", "hi", "hey", "hola", "hei", "hallo"]
        user_lower = user_message.lower().strip()
        
        if any(greeting in user_lower for greeting in greetings):
            return self.get_greeting(self.language)
        
        return None

    def get_greeting(self, language: str) -> str:
        """Return a greeting message based on the selected language."""
        try:
            greetings_list = chatbot_data.get("greetings", [])
            
            if greetings_list and len(greetings_list) > 0:
                greeting_obj = greetings_list[0]
                language_greetings = greeting_obj.get("replies", {}).get(
                    language, ["Hello! How can I assist you today?"]
                )
                
                if isinstance(language_greetings, list) and language_greetings:
                    return random.choice(language_greetings)
            
            return "Hello! How can I assist you today?"
            
        except Exception as e:
            logger.error(f"Error getting greeting: {str(e)}")
            return "Hello! How can I assist you today?"

    def _get_fallback_response(self) -> str:
        """Return a fallback response when the chatbot doesn't understand."""
        try:
            fallbacks_list = chatbot_data.get("fallbacks", [])
            
            if fallbacks_list and len(fallbacks_list) > 0:
                fallback_obj = fallbacks_list[0]
                language_fallbacks = fallback_obj.get("replies", {}).get(
                    self.language, ["I'm sorry, I didn't understand that."]
                )
                
                if isinstance(language_fallbacks, list) and language_fallbacks:
                    return random.choice(language_fallbacks)
            
            return "I'm sorry, I didn't understand that."
            
        except Exception as e:
            logger.error(f"Error getting fallback: {str(e)}")
            return "I'm sorry, I didn't understand that."
