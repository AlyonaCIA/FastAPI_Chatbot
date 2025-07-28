# FastAPI Chatbot

A production-ready chatbot API built with FastAPI that uses TF-IDF vectorization and cosine similarity for natural language processing and response generation.

## Overview

This project implements a RESTful chatbot service with session management, structured response matching, and comprehensive testing. The application is containerized and includes a complete CI/CD pipeline for automated testing and deployment.

## Features

- FastAPI-based REST API with automatic OpenAPI documentation
- Natural language processing using TF-IDF vectorization and cosine similarity
- UUID-based session management for conversation tracking
- Structured logging for monitoring and debugging
- Comprehensive test suite with unit and integration tests
- Docker containerization for consistent deployments
- Automated CI/CD pipeline with GitHub Actions

## Architecture

```
backend/
├── main.py                    # Application entry point
├── schemas.py                 # Pydantic models for request/response validation
├── config/
│   └── data_loader.py         # Data loading utilities
├── data/
│   └── kindly-bot.json        # Chatbot training data
├── services/
│   └── chatbot_service.py     # Core chatbot logic
├── utils/
│   └── session_manager.py     # Session handling utilities
└── test/
    ├── unit_test/             # Unit tests
    └── integration_test/       # Integration tests
```

## API Endpoints

### Start Conversation
```http
POST /api/conversation/start?language=en
```

Response:
```json
{
    "session_id": "uuid-string",
    "message": "Hello! I am a chatbot.",
    "success": true
}
```

### Send Message
```http
POST /api/conversation/message
```

Request:
```json
{
    "user_id": "uuid-string",
    "message": "user message"
}
```

Response:
```json
{
    "session_id": "uuid-string",
    "message": "chatbot response",
    "success": true
}
```

### Debug Sessions
```http
GET /api/debug/sessions
```

Returns list of active sessions for debugging purposes.

## Installation

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-chatbot
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8080 --reload
```

The API documentation will be available at `http://localhost:8080/docs`

### Docker Deployment

1. Build the image:
```bash
docker build -t fastapi-chatbot .
```

2. Run the container:
```bash
docker run -p 8080:8080 fastapi-chatbot
```

## Testing

Run unit tests:
```bash
pytest backend/test/unit_test/
```

Run integration tests:
```bash
pytest backend/test/integration_test/
```

Run all tests with coverage:
```bash
pytest --cov=backend
```

## Development

### Code Quality

The project uses the following tools for code quality:
- `flake8` for linting
- `isort` for import sorting
- `autopep8` for code formatting

Run quality checks:
```bash
flake8 backend/
isort backend/
autopep8 --recursive --in-place backend/
```

### CI/CD Pipeline

The GitHub Actions workflow automatically:
- Runs code quality checks
- Executes the full test suite
- Builds and validates Docker images
- Performs security scans

## Configuration

The application can be configured through environment variables:
- `LOG_LEVEL`: Logging level (default: INFO)
- `PORT`: Application port (default: 8080)
- `HOST`: Application host (default: 0.0.0.0)

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Ensure all tests pass and code quality checks succeed
5. Submit a pull request with a clear description of changes

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Author

Alyona Carolina Ivanova Araujo  
Email: alenacivanovaa@gmail.com
