"""Module for Chatbot Serrvices."""
# ✅ Standard Library Imports
import logging
from typing import List, Tuple

# ✅ Third-Party Imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Local Application Imports
from backend.config.data_loader import chatbot_data

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChatbotService:
    """Handles chatbot logic and response generation using NLP."""

    def __init__(self):
        """Initialize the chatbot with TF-IDF vectorization and load training data."""
        self.language = "en"
        self.questions, self.answers = self._load_data()

        if not self.questions:
            raise ValueError("❌ No training data found. Check JSON structure.")

        # Configurar vectorizador TF-IDF para preguntas
        self.vectorizer = TfidfVectorizer(
            min_df=1,
            strip_accents='unicode',
            lowercase=True,
            # Considera unigramas y bigramas para mejorar coincidencias
            ngram_range=(1, 2)
        )
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

        logger.info(
            f"✅ ChatbotService initialized with {len(self.questions)} QA pairs.")

    def _load_data(self) -> Tuple[List[str], List[str]]:
        """Extracts questions and answers from chatbot_data."""
        questions, answers = [], []

        try:
            for dialogue in chatbot_data.get("dialogues", []):
                samples = dialogue.get("samples", {}).get(self.language, [])
                replies = dialogue.get("replies", {}).get(self.language, [])

                if not replies:
                    logger.warning(
                        f"⚠️ No replies found for dialogue ID: {dialogue.get('id', 'unknown')}")
                    continue

                for sample in samples:
                    if not isinstance(sample, str) or not sample.strip():
                        continue
                    questions.append(sample.lower().strip())
                    # Tomamos la primera respuesta como principal
                    answers.append(replies[0])

            logger.info(
                f"📥 Successfully loaded {len(questions)} questions and {len(answers)} answers.")
            return questions, answers

        except Exception as e:
            logger.error(f"❌ Error loading chatbot data: {str(e)}")
            raise

    def process_message(self, user_message: str) -> str:
        """Finds the most relevant response using NLP similarity matching."""
        if not user_message or not user_message.strip():
            return self._get_fallback_response()

        try:
            user_message = user_message.lower().strip()
            logger.debug(f"📩 Processing user message: '{user_message}'")

            user_vector = self.vectorizer.transform([user_message])
            similarities = cosine_similarity(
                user_vector, self.question_vectors).flatten()

            best_match_idx = similarities.argmax()
            confidence = similarities[best_match_idx]

            logger.debug(f"🔍 Best match confidence: {confidence:.4f}")

            if confidence < 0.3:
                logger.info(
                    f"⚠️ Low confidence ({confidence:.2f}) for message: '{user_message}'. Returning fallback response.")
                return self._get_fallback_response()

            matched_question = self.questions[best_match_idx]
            logger.info(
                f"✅ Matched '{user_message}' to '{matched_question}' with confidence {confidence:.2f}")

            return self.answers[best_match_idx]

        except Exception as e:
            logger.error(f"❌ Error processing message: {str(e)}")
            return self._get_fallback_response()

    def get_greeting(self, language: str) -> str:
        """Returns a greeting message based on the selected language."""
        greetings = chatbot_data.get("greetings", {})

        if isinstance(
                greetings, dict):  # ✅ Accedemos a la clave 'replies' correctamente
            language_greetings = greetings.get("replies", {}).get(
                language, ["Hello! How can I assist you today?"])
            if isinstance(language_greetings, list) and language_greetings:
                # 🔥 Tomamos solo el primer mensaje disponible
                return language_greetings[0]

        return "Hello! How can I assist you today?"

    def _get_fallback_response(self) -> str:
        """Returns a fallback response when the chatbot does not understand the
        message."""
        try:
            return chatbot_data.get("fallbacks", [{}])[0].get("replies", {}).get(
                self.language, ["I'm sorry, I didn't understand that."])[0]
        except (IndexError, AttributeError):
            return "I'm sorry, I didn't understand that."


# Crear una única instancia del chatbot para evitar múltiples cargas de datos
chatbot_service = ChatbotService()
