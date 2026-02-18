.PHONY: help install install-dev sync update clean test test-cov lint format type-check security audit run dev docker-build docker-run pre-commit ci

# Default target
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

## help: Display this help message
help:
	@echo "$(BLUE)FastAPI Chatbot - Development Commands$(NC)"
	@echo ""
	@echo "$(GREEN)Setup:$(NC)"
	@echo "  make install         Install production dependencies with uv"
	@echo "  make install-dev     Install all dependencies including dev tools"
	@echo "  make sync            Sync dependencies from lock file"
	@echo "  make update          Update dependencies to latest versions"
	@echo ""
	@echo "$(GREEN)Development:$(NC)"
	@echo "  make run             Run the application"
	@echo "  make dev             Run in development mode with auto-reload"
	@echo "  make format          Format code with black and ruff"
	@echo "  make lint            Run all linters (ruff + flake8 if present)"
	@echo "  make type-check      Run mypy type checking"
	@echo "  make test            Run tests"
	@echo "  make test-cov        Run tests with coverage report"
	@echo "  make security        Run security checks (bandit)"
	@echo "  make audit           Audit dependencies for vulnerabilities"
	@echo "  make pre-commit      Run pre-commit hooks on all files"
	@echo "  make ci              Run full CI pipeline locally"
	@echo ""
	@echo "$(GREEN)Docker:$(NC)"
	@echo "  make docker-build    Build Docker image"
	@echo "  make docker-run      Run Docker container"
	@echo ""
	@echo "$(GREEN)Cleanup:$(NC)"
	@echo "  make clean           Remove build artifacts and cache files"
	@echo ""

## install: Install production dependencies
install:
	@echo "$(BLUE)Installing production dependencies with uv...$(NC)"
	@uv pip install -e .

## install-dev: Install all dependencies including dev tools
install-dev:
	@echo "$(BLUE)Installing all dependencies with uv...$(NC)"
	@uv pip install -e ".[dev]"
	@echo "$(GREEN)Installing pre-commit hooks...$(NC)"
	@pre-commit install

## sync: Sync dependencies from lock file
sync:
	@echo "$(BLUE)Syncing dependencies from uv.lock...$(NC)"
	@uv sync

## update: Update dependencies to latest versions
update:
	@echo "$(BLUE)Updating dependencies...$(NC)"
	@uv lock --upgrade
	@uv sync

## clean: Remove build artifacts and cache files
clean:
	@echo "$(YELLOW)Cleaning build artifacts and cache files...$(NC)"
	@rm -rf build/ dist/ *.egg-info
	@rm -rf .pytest_cache .ruff_cache .mypy_cache .coverage htmlcov
	@rm -rf **/__pycache__ **/*.pyc **/*.pyo
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name ".DS_Store" -delete
	@echo "$(GREEN)Clean complete!$(NC)"

## format: Format code with black and ruff
format:
	@echo "$(BLUE)Formatting code with black...$(NC)"
	@uv run black app tests
	@echo "$(BLUE)Sorting imports with ruff...$(NC)"
	@uv run ruff check --select I --fix app tests
	@echo "$(GREEN)Formatting complete!$(NC)"

## lint: Run all linters
lint:
	@echo "$(BLUE)Running ruff linter...$(NC)"
	@uv run ruff check app tests
	@echo "$(GREEN)Linting complete!$(NC)"

## type-check: Run mypy type checking
type-check:
	@echo "$(BLUE)Running mypy type checker...$(NC)"
	@uv run mypy app --ignore-missing-imports
	@echo "$(GREEN)Type checking complete!$(NC)"

## test: Run tests
test:
	@echo "$(BLUE)Running tests...$(NC)"
	@uv run pytest tests/

## test-cov: Run tests with coverage
test-cov:
	@echo "$(BLUE)Running tests with coverage...$(NC)"
	@uv run pytest --cov=app --cov-report=term-missing --cov-report=html
	@echo "$(GREEN)Coverage report generated in htmlcov/index.html$(NC)"

## security: Run security checks
security:
	@echo "$(BLUE)Running bandit security checks...$(NC)"
	@uv run bandit -r app -ll
	@echo "$(GREEN)Security check complete!$(NC)"

## audit: Audit dependencies for vulnerabilities
audit:
	@echo "$(BLUE)Auditing dependencies...$(NC)"
	@uv pip list --format=json | python -m json.tool
	@echo "$(YELLOW)Note: Use 'pip-audit' or external tools for vulnerability scanning$(NC)"

## pre-commit: Run pre-commit hooks on all files
pre-commit:
	@echo "$(BLUE)Running pre-commit hooks...$(NC)"
	@pre-commit run --all-files

## ci: Run full CI pipeline locally
ci: clean format lint type-check test-cov security
	@echo "$(GREEN)✓ CI pipeline complete!$(NC)"

## run: Run the application
run:
	@echo "$(BLUE)Starting FastAPI Chatbot...$(NC)"
	@uv run python -m app.main

## dev: Run in development mode with auto-reload
dev:
	@echo "$(BLUE)Starting FastAPI Chatbot in development mode...$(NC)"
	@uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

## docker-build: Build Docker image
docker-build:
	@echo "$(BLUE)Building Docker image...$(NC)"
	@docker build -t fastapi-chatbot:latest .
	@echo "$(GREEN)Docker image built successfully!$(NC)"

## docker-run: Run Docker container
docker-run:
	@echo "$(BLUE)Running Docker container...$(NC)"
	@docker run -d --name fastapi-chatbot -p 8080:8080 fastapi-chatbot:latest
	@echo "$(GREEN)Container running at http://localhost:8080$(NC)"
