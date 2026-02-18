# FastAPI Chatbot

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](http://mypy-lang.org/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

> **Author:** Alyona Carolina Ivanova Araujo  
> **Email:** alenacivanovaa@gmail.com  
> **Version:** 1.0.1

A **production-ready** chatbot API built with FastAPI that leverages TF-IDF vectorization and cosine similarity for intelligent natural language processing and response generation.

## Overview

This project implements a RESTful chatbot service following **Clean Architecture** principles with comprehensive session management, structured response matching, and enterprise-grade development tooling. The application is fully containerized and includes a complete **CI/CD pipeline** for automated testing, quality assurance, and deployment.

### Why This Project Stands Out

- **Clean Architecture**: Proper separation of concerns with domain-driven design
- **Test-Driven Development**: Comprehensive unit and integration tests with 70%+ coverage
- **CI/CD Ready**: Full GitHub Actions pipeline with matrix testing
- **Modern Tooling**: Nox, pre-commit hooks, black, isort, flake8, mypy, safety
- **Production Ready**: Docker support, structured logging, environment-based configuration
- **Multilingual**: English and Norwegian support out of the box
- **Type Safe**: Full type hints with mypy static type checking

## Key Features

### Core Functionality
- **FastAPI Framework**: High-performance async REST API with automatic OpenAPI/Swagger documentation
- **NLP Engine**: TF-IDF vectorization with cosine similarity for intelligent response matching
- **Session Management**: UUID-based conversation tracking with configurable TTL
- **Multilingual Support**: English (`en`) and Norwegian (`nb`) with extensible language system
- **Confidence Scoring**: Adjustable threshold for response quality control

### Architecture & Design
- **Clean Architecture**: Domain-centric design with dependency inversion principle
- **Repository Pattern**: Abstracted data access with interface-based design
- **Dependency Injection**: Loose coupling through FastAPI's DI system
- **Factory Pattern**: Centralized object creation and lifecycle management
- **Service Layer**: Business logic isolated from HTTP and infrastructure concerns

### Development Excellence
- **Comprehensive Testing**: Unit tests, integration tests, and API endpoint tests
- **Code Coverage**: 70%+ coverage with HTML and XML reports
- **Code Formatting**: Black (88 chars) + isort with pre-commit hooks
- **Static Analysis**: flake8 linting + mypy type checking
- **Security Scanning**: Automated dependency vulnerability checks with Safety
- **Nox Automation**: Isolated test environments matching CI/CD pipeline
- **Pre-commit Hooks**: Automated quality checks before every commit

### DevOps & Deployment
- **Docker Ready**: Full containerization with docker-compose support
- **CI/CD Pipeline**: GitHub Actions with matrix testing (Python 3.11, 3.12)
- **Package Management**: Setuptools configuration with versioning
- **Configuration Management**: Environment-based settings with pydantic-settings
- **Structured Logging**: Configurable log levels and formatting
- **CORS Support**: Configurable cross-origin resource sharing

## Quick Start

Get up and running in minutes:

```bash
# 1. Clone the repository
git clone https://github.com/AlyonaCIA/FastAPI_Chatbot.git
cd FastAPI_Chatbot

# 2. Setup development environment (recommended)
./run_local.sh -i

# 3. Run the application
python -m app.main

# 4. Test the API
curl -X POST "http://localhost:8080/api/v1/conversations/start" \
  -H "Content-Type: application/json" \
  -d '{"language": "en"}'

# 5. View interactive documentation
open http://localhost:8080/docs
```

The API will be available at `http://localhost:8080` with:
- **Swagger UI**: `http://localhost:8080/docs`
- **ReDoc**: `http://localhost:8080/redoc`
- **OpenAPI Schema**: `http://localhost:8080/openapi.json`

## Technology Stack

### Core Framework & Runtime
- **Python 3.11/3.12**: Modern Python with latest performance improvements
- **FastAPI 0.109.0**: High-performance async web framework
- **Uvicorn 0.27.0**: Lightning-fast ASGI server
- **Pydantic 2.6.0**: Data validation and settings management with pydantic-settings

### NLP & Data Processing
- **scikit-learn 1.4.0**: TF-IDF vectorization and cosine similarity
- **cachetools 6.1.0**: Response caching for performance optimization

### Development & Quality Tools
- **Nox 2023.4.22**: Automated testing in isolated environments
- **pytest 8.0.0**: Modern Python testing framework with plugins
  - pytest-cov: Code coverage measurement
  - pytest-mock: Mock object integration
  - pytest-asyncio: Async test support
- **Black 24.1.0**: Uncompromising code formatter (88 char line length)
- **isort 5.13.0**: Import statement organizer with black compatibility
- **flake8 7.0.0**: Style guide enforcement (PEP 8)
- **mypy 1.8.0**: Static type checker for type safety
- **Safety 3.0.0**: Dependency security vulnerability scanner
- **pre-commit 3.6.0**: Git hook framework for automated quality checks
  - Trailing whitespace removal
  - YAML validation
  - Large file detection
  - Branch protection (dev/main)
  - Docstring formatting
  - Typo detection

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

Ensure you have the following installed:
- **Python 3.11 or 3.12** (3.12 recommended for latest features)
- **pip** (latest version: `pip install --upgrade pip`)
- **git** for cloning the repository
- **Virtual environment** (venv or virtualenv)
- **(Optional) Docker** for containerized deployment

### Local Development Setup

#### Option 1: Quick Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/AlyonaCIA/FastAPI_Chatbot.git
cd FastAPI_Chatbot

# One-command setup (installs everything)
./run_local.sh -i

# Verify installation
python -m app.main
```

#### Option 2: Manual Setup

```bash
# 1. Clone the repository
git clone https://github.com/AlyonaCIA/FastAPI_Chatbot.git
cd FastAPI_Chatbot

# 2. Create virtual environment
python3.11 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install production dependencies
pip install -r requirements.txt

# 6. Install development dependencies (for contributors)
pip install -r requirements-dev.txt

# 7. Install pre-commit hooks (optional but recommended)
pre-commit install

# 8. Verify installation
python -m pytest tests/
```

### Environment Configuration

Create a `.env` file for custom configuration (optional):

```bash
# .env
DEBUG=false
LOG_LEVEL=INFO
HOST=0.0.0.0
PORT=8080
DEFAULT_LANGUAGE=en
CONFIDENCE_THRESHOLD=0.3
SESSION_TTL_HOURS=24
MAX_SESSIONS=1000
```

### Running the Application

```bash
# Development mode (auto-reload enabled)
python -m app.main

# Or with uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8080 --workers 4
```

Access the API:
- **API Base**: http://localhost:8080
- **Swagger Docs**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

### Docker Deployment

For containerized deployment:

```bash
# Build Docker image
docker build -t fastapi-chatbot:latest .

# Run container
docker run -d \
  --name fastapi-chatbot \
  -p 8080:8080 \
  -e DEBUG=false \
  -e LOG_LEVEL=INFO \
  fastapi-chatbot:latest

# View logs
docker logs -f fastapi-chatbot

# Stop container
docker stop fastapi-chatbot

# Or use docker-compose
docker-compose up -d --build

# View docker-compose logs
docker-compose logs -f
```

**Docker Features:**
- Production-ready multi-stage build
- Minimal image size with alpine base
- Non-root user for security
- Health checks included
- Structured logging to stdout

## Development

### Development Environment Setup

The project provides a comprehensive development script that mirrors the CI/CD pipeline:

```bash
# One-time setup - Install all dev dependencies and tools
./run_local.sh -i

# Format code (black + isort)
./run_local.sh -f

# Run linting checks (flake8 + mypy)
./run_local.sh -l

# Run all tests with coverage
./run_local.sh -t

# Run security scan
./run_local.sh -s

# Run complete CI pipeline locally (recommended before pushing)
./run_local.sh -n

# Help and options
./run_local.sh -h
```

### Using Nox (Recommended Workflow)

Nox provides isolated virtual environments for each task, ensuring reproducibility:

```bash
# List all available sessions
nox -l

# Format code automatically
nox -s format

# Check formatting without modifying (CI mode)
nox -s format -- --check

# Run linting (flake8 + mypy)
nox -s lint

# Run tests with coverage (single Python version)
nox -s tests

# Run tests across all Python versions (3.11, 3.12)
nox -s tests --python 3.11 3.12

# Run security vulnerability scan
nox -s security

# Clean all build artifacts and caches
nox -s clean

# Run complete CI pipeline (format check + lint + tests + security)
nox -s ci
```

### Pre-commit Hooks

Install pre-commit hooks to automatically enforce code quality standards:

```bash
# Install hooks (one-time setup)
pre-commit install

# Manually run hooks on all files
pre-commit run --all-files

# Update hook versions
pre-commit autoupdate
```

**Pre-commit checks include:**
- Trailing whitespace removal
- End-of-file fixer
- YAML syntax validation
- Large file detection (>500KB)
- Branch protection (prevents commits to dev/main)
- Docstring formatting (88 char wrap)
- Import sorting (isort)
- Code linting (flake8)
- Typo detection

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

The project includes a comprehensive GitHub Actions workflow that ensures code quality and reliability.

### Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Actions Pipeline                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │ Code Quality │  │    Testing    │  │  Build & Deploy │  │
│  ├──────────────┤  ├──────────────┤  ├─────────────────┤  │
│  │ • Format ✓   │  │ • Python 3.11│  │ • Package Build │  │
│  │ • Lint ✓     │  │ • Python 3.12│  │ • Docker Image  │  │
│  │ • Type Check │  │ • Coverage   │  │ • Artifacts     │  │
│  │ • Security   │  │ • JUnit XML  │  │ • Reports       │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### CI/CD Jobs

#### 1. **Code Quality & Security**
- **Black & isort**: Code formatting validation
- **flake8**: PEP 8 compliance and linting
- **mypy**: Static type checking
- **Safety**: Dependency vulnerability scanning
- **Exit on failure**: Pipeline stops if quality checks fail

#### 2. **Matrix Testing**
- **Python Versions**: 3.11, 3.12
- **Parallel Execution**: Tests run simultaneously
- **Coverage Reports**: HTML, XML, and terminal output
- **JUnit XML**: Test result artifacts for analysis
- **Minimum Coverage**: 70% threshold enforced

#### 3. **Nox Validation**
- **Isolated Environments**: Replicates production conditions
- **Full Pipeline**: format → lint → test → security
- **Dependency Caching**: Faster builds with pip cache
- **Artifact Upload**: Coverage reports and test results

#### 4. **Integration Testing**
- **API Workflow**: Real conversation flow testing
- **Session Management**: UUID tracking validation
- **Multi-language**: English and Norwegian responses
- **Health Checks**: Endpoint availability verification

#### 5. **Build Verification**
- **Setup.py**: Package building and installation
- **Dependency Resolution**: Requirements validation
- **Import Testing**: Module accessibility checks

### Trigger Conditions

The pipeline runs automatically on:
- **Push** to `main`, `develop`, or `feature/*` branches
- **Pull Requests** targeting `main` or `develop`
- **Manual Dispatch**: Workflow can be triggered manually

### Caching Strategy

Optimized build times through intelligent caching:
- **Pip Dependencies**: Cached per Python version
- **Nox Environments**: Cached per session
- **Cache Key**: Based on requirements files hash

### Artifacts & Reports

Generated artifacts include:
- **Test Results**: JUnit XML format
- **Coverage Reports**: HTML and XML
- **Security Scan**: JSON vulnerability report
- **Retention**: 30 days for all artifacts

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

We welcome contributions from the community! Please follow these guidelines to ensure a smooth collaboration.

### Development Guidelines

1. **Follow Clean Architecture**: Maintain separation between domain, infrastructure, and API layers
2. **Write Tests First**: TDD approach - write tests before implementing features
3. **Maintain Coverage**: Keep code coverage above 70%
4. **Type Everything**: Use type hints for all function parameters and return values
5. **Document Code**: Add docstrings to all classes and public methods
6. **Conventional Commits**: Use clear, descriptive commit messages
7. **Run Quality Checks**: Ensure all CI checks pass before submitting PR

### Contribution Workflow

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/FastAPI_Chatbot.git
cd FastAPI_Chatbot

# 3. Create a feature branch from main
git checkout main
git pull origin main
git checkout -b feature##/your-feature-name

# 4. Install development dependencies
./run_local.sh -i

# 5. Install pre-commit hooks
pre-commit install

# 6. Make your changes following TDD
# - Write tests first (tests/)
# - Implement feature
# - Run tests: nox -s tests

# 7. Run all quality checks locally
nox -s ci
# or
./run_local.sh -n

# 8. Commit with conventional commit message
git add .
git commit -m "feat: add new feature description"

# 9. Push to your fork
git push origin feature##/your-feature-name

# 10. Open a Pull Request on GitHub
# - Target branch: main
# - Fill out PR template
# - Wait for CI to pass
# - Request review
```

### Branch Naming Convention

Follow the repository's naming pattern:
- `feature##/description` - New features (e.g., `feature04/add-dual-license`)
- `bugfix##/description` - Bug fixes
- `docs##/description` - Documentation updates
- `refactor##/description` - Code refactoring

### Commit Message Format

Use conventional commits for clear history:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
feat(api): add conversation history endpoint
fix(chatbot): resolve TF-IDF vectorization edge case
docs(readme): update installation instructions
test(domain): add session service unit tests
```

### Code Standards

#### Python Style
- **Line Length**: 88 characters (Black default)
- **Import Sorting**: isort with black profile
- **Docstring Style**: Google-style docstrings
- **Naming Conventions**:
  - Classes: `PascalCase`
  - Functions/Variables: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`
  - Private members: `_leading_underscore`

#### Type Hints
```python
from typing import List, Optional, Dict

def process_message(
    message: str,
    session_id: str,
    metadata: Optional[Dict[str, str]] = None
) -> List[str]:
    """Process incoming message."""
    pass
```

#### Testing Requirements
- Unit tests for all business logic
- Integration tests for API endpoints
- Minimum 70% code coverage
- Test file naming: `test_*.py`
- Test function naming: `test_<feature>_<scenario>()`

### Pull Request Checklist

Before submitting, ensure:
- [ ] Code follows project style guide
- [ ] All tests pass (`nox -s tests`)
- [ ] Code coverage is maintained or improved
- [ ] Type checking passes (`nox -s lint`)
- [ ] Security scan passes (`nox -s security`)
- [ ] Documentation is updated (if needed)
- [ ] Commit messages follow conventional format
- [ ] Branch is up to date with main
- [ ] No conflicts with main branch

### Getting Help

- **Email**: alenacivanovaa@gmail.com
- **Documentation**: Check `/docs` folder
- **Bug Reports**: Open an issue with detailed description
- **Feature Requests**: Open an issue with use case explanation

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

**Copyright © 2024-2026 Alyona Carolina Ivanova Araujo**

This project is available under a **dual licensing model** to support both open-source community and commercial use:

### Free License: AGPL-3.0

The following users can use this software **FREE** under the GNU Affero General Public License v3.0:

| User Type | Use Case | Cost |
|-----------|----------|------|
| **Individual Developers** | Personal projects, learning, portfolio | **FREE** |
| **Educational Institutions** | Universities, schools, research, teaching | **FREE** |
| **Students & Researchers** | Academic projects, thesis work | **FREE** |
| **Non-Profit Organizations** | Charitable work, community projects | **FREE** |
| **Open Source Projects** | AGPL-compatible projects, contributions | **FREE** |

**Requirements:**
- Source code modifications must be disclosed
- Derivative works must use AGPL-3.0
- Network use triggers copyleft (AGPL provision)
- Attribution to original author required

### Commercial License

**For-profit companies** and commercial entities must obtain a commercial license:

| User Type | When Required |
|-----------|---------------|
| **Companies** | Using software in any commercial capacity |
| **For-Profit Orgs** | Revenue-generating products or services |
| **SaaS Providers** | Hosting as a service for customers |
| **Product Integration** | Embedding in proprietary software |

**Benefits:**
- No source code disclosure required
- No copyleft obligations
- Proprietary use allowed
- Priority support & maintenance
- Custom feature development available
- Legal protection & indemnification

**To obtain a commercial license:**
- Email: alenacivanovaa@gmail.com
- Subject: "FastAPI Chatbot - Commercial License Request"
- Include: Company name, use case, number of developers

### Licensing FAQ

**Q: I'm a freelancer building a client project. Which license?**  
A: If your client is a commercial entity, they need a commercial license. If you're doing non-profit work, AGPL-3.0 applies.

**Q: Can I use this for my startup?**  
A: If your startup is a registered business or generating revenue, you need a commercial license.

**Q: What if I modify the code?**  
A: Under AGPL-3.0, you must share modifications. Under commercial license, modifications are proprietary.

**Q: University spin-off company?**  
A: Company = Commercial license. University research project = AGPL-3.0.

For complete legal terms, see the [LICENSE](LICENSE) file.

**Questions?** Contact: alenacivanovaa@gmail.com

---

## Author

<div align="center">

### Alyona Carolina Ivanova Araujo

**Software Engineer | Python Developer | API Architect**

**Email:** alenacivanovaa@gmail.com  
**GitHub:** [@AlyonaCIA](https://github.com/AlyonaCIA)  
**Version:** 1.0.1

---

### Project Stats

![Python Version](https://img.shields.io/badge/Python-3.11%20|%203.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688)
![Code Coverage](https://img.shields.io/badge/Coverage-70%25+-success)
![License](https://img.shields.io/badge/License-AGPL--3.0%20|%20Commercial-blue)

</div>

---

## Acknowledgments

This project was built with:
- Modern Python best practices and tooling
- Clean Architecture principles
- Test-Driven Development methodology
- Comprehensive CI/CD pipeline
- Community-driven open source values

---

<div align="center">

**If you find this project useful, please consider giving it a star!**

Made with care by Alyona Carolina Ivanova Araujo

</div>
