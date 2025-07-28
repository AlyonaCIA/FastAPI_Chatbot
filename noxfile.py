"""Nox configuration for FastAPI Chatbot - Compatible with GitHub Actions."""
import nox

PYTHON_VERSIONS = ["3.11", "3.12"]
DEFAULT_PYTHON = "3.11"

@nox.session(python=DEFAULT_PYTHON)
def format(session):
    """Format code with black and isort."""
    session.install("-r", "requirements-dev.txt")
    
    # Check if --check flag is passed for CI
    check_only = "--check" in session.posargs
    
    if check_only:
        session.run("black", "--check", "--diff", "app", "tests")
        session.run("isort", "--check-only", "--diff", "app", "tests")
    else:
        session.run("black", "app", "tests")
        session.run("isort", "app", "tests")

@nox.session(python=DEFAULT_PYTHON)
def lint(session):
    """Run linting checks."""
    session.install("-r", "requirements-dev.txt")
    session.run("flake8", "app", "tests")
    session.run("mypy", "app", "--ignore-missing-imports")

@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run tests with pytest."""
    session.install("-r", "requirements-dev.txt")
    
    # Create junit directory
    session.run("mkdir", "-p", "junit", external=True)
    
    session.run(
        "pytest", 
        "--cov=app", 
        "--cov-report=term-missing",
        "--cov-report=html:htmlcov",
        "--cov-report=xml:coverage.xml",
        "--junitxml=junit/test-results.xml",
        "-v"
    )

@nox.session(python=DEFAULT_PYTHON)
def security(session):
    """Run security checks."""
    session.install("-r", "requirements-dev.txt")
    session.run("safety", "check", "--json", "--output", "safety-report.json")

@nox.session(python=DEFAULT_PYTHON)
def clean(session):
    """Clean up build artifacts and cache files."""
    session.run("rm", "-rf", ".pytest_cache", "htmlcov", ".coverage", 
                "__pycache__", ".mypy_cache", "junit", "safety-report.json",
                "coverage.xml", external=True)
    session.run("find", ".", "-name", "*.pyc", "-delete", external=True)

@nox.session(python=DEFAULT_PYTHON, name="ci")
def ci(session):
    """Run full CI pipeline locally (mirrors GitHub Actions)."""
    session.notify("format", ["--check", "--diff"])
    session.notify("lint")
    session.notify("tests")
    session.notify("security")
