#!/usr/bin/env bash
# This script runs unit tests and security audits on the FastAPI Chatbot codebase.

set -e

# Source message handler functions
source "$(dirname "$0")/message-handler.sh"

# Configuration for this project
PROJECT_NAME="app"
COVERAGE_THRESHOLD=70

# Function to setup test environment
setup_test_environment() {
    info "Setting up test environment for FastAPI Chatbot"

    # Create necessary directories
    mkdir -p junit
    mkdir -p htmlcov

    # Install dependencies
    if [[ -f "requirements.txt" ]]; then
        info "Installing main requirements"
        pip install -r requirements.txt
    fi

    if [[ -f "requirements-dev.txt" ]]; then
        info "Installing development requirements"
        pip install -r requirements-dev.txt
    fi
}

# Function to run pytest tests
run_pytest() {
    info "Running pytest tests"

    pytest tests/ \
        --verbose \
        --tb=short \
        --strict-markers \
        --strict-config \
        --cov=$PROJECT_NAME \
        --cov-branch \
        --cov-report=term-missing:skip-covered \
        --cov-report=html:htmlcov \
        --cov-report=xml:coverage.xml \
        --junitxml=junit/test-results.xml \
        --cov-fail-under=$COVERAGE_THRESHOLD

    local test_exit_code=$?

    if [ $test_exit_code -eq 0 ]; then
        success "All tests passed!"
        info "Coverage report generated in htmlcov/"
    else
        error "Some tests failed"
        info "Check junit/test-results.xml for detailed results"
        exit 1
    fi
}

# Function to run security audit
run_security_audit() {
    info "Running security audit"

    if command -v safety &> /dev/null; then
        safety check --json --output safety-report.json || {
            warning "Security issues found (check safety-report.json)"
        }
    else
        warning "Safety not installed, skipping security audit"
    fi
}

# Main execution
step "Starting test execution for FastAPI Chatbot"

setup_test_environment
run_pytest
run_security_audit

success "Test execution completed successfully!"
info "Reports available:"
info "  - JUnit: junit/test-results.xml"
info "  - Coverage HTML: htmlcov/index.html"
info "  - Coverage XML: coverage.xml"
