# FastAPI Chatbot

A production-ready chatbot API built with FastAPI that uses TF-IDF vectorization and cosine similarity for natural language processing and response generation.

## Overview

This project implements a RESTful chatbot service following clean architecture principles with comprehensive session management, structured response matching, and enterprise-grade development tooling. The application is containerized and includes a complete CI/CD pipeline for automated testing and deployment.

## Features

- **FastAPI-based REST API** with automatic OpenAPI documentation
- **Natural Language Processing** using TF-IDF vectorization and cosine similarity
- **Clean Architecture** with separation of concerns across domain, infrastructure, and API layers
- **UUID-based session management** for conversation tracking
- **Multilingual support** (English and Norwegian)
- **Comprehensive test suite** with unit and integration tests
- **Development tooling** with nox, pre-commit hooks, and automated formatting
- **CI/CD pipeline** with GitHub Actions
- **Docker containerization** for consistent deployments

## Architecture

The project follows clean architecture principles with clear separation of concerns:

```
app/
├── main.py                     # Application entry point
├── core/                       # Application configuration and utilities
│   ├── config.py               # Centralized settings management
│   ├── exceptions.py           # Custom exception definitions
│   └── logging.py              # Logging configuration
├── api/                        # HTTP layer (FastAPI routes and schemas)
│   ├── dependencies.py         # Dependency injection setup
│   └── v1/                     # API versioning
│       ├── routes/             # HTTP endpoints
│       │   ├── conversation.py # Conversation management endpoints
│       │   └── health.py       # Health check endpoints
│       └── schemas/            # Request/response models
│           ├── conversation.py # Conversation-related schemas
│           └── common.py       # Shared schemas
├── domain/                     # Business logic layer
│   ├── entities/               # Domain objects
│   │   └── session.py          # Session entity
│   ├── repositories/           # Repository interfaces
│   │   └── session.py          # Session repository interface
│   └── services/               # Business logic services
│       ├── chatbot.py          # Core chatbot logic
│       └── session.py          # Session management service
└── infrastructure/             # External concerns layer
    ├── data/                   # Data access and loading
    │   ├── datasets/           # Training data
    │   │   └── data-bot.json # Chatbot conversation data
    │   └── loaders/            # Data loading utilities
    │       └── chatbot_data.py # JSON data loader
    └── repositories/           # Repository implementations
        └── memory/             # In-memory implementations
            └── session.py      # In-memory session repository
```

### Design Patterns

- **Repository Pattern**: Abstracts data access with interfaces and implementations
- **Dependency Injection**: Loose coupling through FastAPI's dependency system
- **Service Layer**: Encapsulates business logic separate from HTTP concerns
- **Factory Pattern**: Centralized object creation in dependencies
- **Clean Architecture**: Domain-centric design with dependency inversion

## API Endpoints

### Start Conversation
```http
POST /api/v1/conversations/start
Content-Type: application/json

{
  "language": "en"
}
```

**Response:**
```json
{
  "session_id": "uuid-string",
  "message": "Hello! I am a chatbot!",
  "success": true
}
```

### Send Message
```http
POST /api/v1/conversations/{session_id}/messages
Content-Type: application/json

{
  "message": "Hello, how are you?"
}
```

**Response:**
```json
{
  "session_id": "uuid-string",
  "message": "I am fine, thank you for asking! What can I do for you today?",
  "success": true
}
```

### Health Check
```http
GET /api/v1/health
```

### Debug Sessions
```http
GET /api/v1/conversations/debug/sessions
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Virtual environment (recommended)

### Local Development

1. **Clone the repository:**
```bash
git clone <repository-url>
cd fastapi-chatbot
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
# Quick setup
./run_local.sh -i

# Or manual installation
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

4. **Run the application:**
```bash
python -m app.main
```

The API will be available at `http://localhost:8080` with interactive documentation at `http://localhost:8080/docs`.

### Docker Deployment

```bash
# Build and run with Docker
docker build -t fastapi-chatbot .
docker run -p 8080:8080 fastapi-chatbot

# Or use docker-compose for development
docker-compose up --build
```

## Development

### Development Workflow

The project includes a comprehensive development script that mirrors the CI pipeline:

```bash
# Setup development environment
./run_local.sh -i

# Format code
./run_local.sh -f

# Run linting
./run_local.sh -l

# Run tests
./run_local.sh -t

# Run full CI pipeline locally
./run_local.sh -n
```

### Using Nox (Recommended)

Nox provides isolated environments for different development tasks:

```bash
# List available sessions
nox -l

# Format code
nox -s format

# Run linting
nox -s lint

# Run tests
nox -s tests

# Run security scan
nox -s security

# Clean artifacts
nox -s clean

# Run CI pipeline
nox -s ci
```

### Code Quality Tools

The project enforces code quality through multiple tools:

- **Black**: Code formatting (88 character line length)
- **isort**: Import sorting with black compatibility
- **flake8**: Code linting and style checking
- **mypy**: Static type checking
- **safety**: Security vulnerability scanning
- **pytest**: Unit and integration testing

### Pre-commit Hooks

Install pre-commit hooks to automatically check code quality:

```bash
pre-commit install
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test types
pytest tests/unit/           # Unit tests only
pytest tests/integration/    # Integration tests only

# Run with coverage
pytest --cov=app --cov-report=html

# Run with nox (isolated environment)
nox -s tests
```

### Test Structure

```
tests/
├── unit/                    # Unit tests
│   ├── domain/              # Domain layer tests
│   └── infrastructure/      # Infrastructure layer tests
├── integration/             # Integration tests
│   └── api/                 # API endpoint tests
└── conftest.py             # Pytest configuration and fixtures
```

## Configuration

The application uses environment variables for configuration:

```bash
# Create .env file (optional)
DEBUG=true
LOG_LEVEL=INFO
HOST=0.0.0.0
PORT=8080
DEFAULT_LANGUAGE=en
CONFIDENCE_THRESHOLD=0.3
SESSION_TTL_HOURS=24
```

### Configuration Options

- `DEBUG`: Enable debug mode (default: false)
- `LOG_LEVEL`: Logging level (default: INFO)
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8080)
- `DEFAULT_LANGUAGE`: Default conversation language (default: en)
- `CONFIDENCE_THRESHOLD`: NLP confidence threshold (default: 0.3)
- `SESSION_TTL_HOURS`: Session time-to-live (default: 24)

## CI/CD Pipeline

The GitHub Actions workflow includes:

### Jobs

1. **Code Quality**: Format checking, linting, and security scanning
2. **Tests**: Matrix testing across Python 3.11 and 3.12
3. **Nox Validation**: Mirrors local development environment
4. **API Integration**: Real API endpoint testing
5. **Build Verification**: Package building and validation

### Workflow Features

- **Matrix Testing**: Multiple Python versions
- **Caching**: Pip dependencies and nox environments
- **Artifacts**: Test results, coverage reports, security scans
- **Integration Testing**: Full API workflow validation
- **Build Verification**: Package creation and installation

### Triggering CI

The pipeline runs on:
- Push to `main`, `develop`, or `feature/*` branches
- Pull requests to `main` or `develop`

## NLP and Chatbot Logic

### Response Selection Algorithm

1. **Greeting Detection**: Checks for common greetings (hello, hi, hey)
2. **Sample Matching**: Uses TF-IDF vectorization and cosine similarity
3. **Keyword Matching**: Falls back to keyword-based responses
4. **Fallback Response**: Default response for unmatched inputs

### Training Data

The chatbot uses structured JSON data (`kindly-bot.json`) with:
- **Greetings**: Welcome messages in multiple languages
- **Dialogues**: Sample-based conversations with replies
- **Keywords**: Topic-based responses
- **Fallbacks**: Default responses for unknown inputs

### Multilingual Support

- English (`en`) and Norwegian (`nb`) support
- Language-specific responses and greetings
- Automatic language detection and validation

## Contributing

### Development Guidelines

1. **Follow clean architecture principles**
2. **Write comprehensive tests for new features**
3. **Maintain code coverage above 70%**
4. **Use conventional commit messages**
5. **Ensure all CI checks pass**

### Contribution Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make changes following coding standards
4. Run local quality checks: `./run_local.sh -n`
5. Commit changes with descriptive messages
6. Push to your fork and submit a pull request

### Code Standards

- **Line Length**: 88 characters (Black default)
- **Import Sorting**: isort with black profile
- **Type Hints**: Required for all public functions
- **Documentation**: Docstrings for all classes and public methods
- **Testing**: Unit tests for business logic, integration tests for APIs

## Performance Considerations

- **Singleton Pattern**: Services are instantiated once per application lifecycle
- **Caching**: TF-IDF vectors are pre-computed and cached
- **Session Management**: Efficient in-memory storage with TTL cleanup
- **Async Support**: Full async/await implementation for scalability
- **Connection Pooling**: Optimized for database connections (future enhancement)

## Security

- **Input Validation**: Pydantic models validate all inputs
- **Dependency Scanning**: Automated security vulnerability checks
- **CORS Configuration**: Configurable cross-origin resource sharing
- **Environment Variables**: Sensitive configuration externalized

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Author

**Alyona Carolina Ivanova Araujo**  
Email: alenacivanovaa@gmail.com

---

## Quick Start

```bash
# 1. Clone and setup
git clone <repository-url>
cd fastapi-chatbot
./run_local.sh -i

# 2. Run the application
python -m app.main

# 3. Test the API
curl -X POST "http://localhost:8080/api/v1/conversations/start" \
  -H "Content-Type: application/json" \
  -d '{"language": "en"}'

# 4. View documentation
open http://localhost:8080/docs
```
