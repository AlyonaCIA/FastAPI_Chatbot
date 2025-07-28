#!/usr/bin/env bash
# This script runs linting checks on FastAPI Chatbot Python files.

set -e

# Source message handler functions
source "$(dirname "$0")/message-handler.sh"

# Configuration
PROJECT_DIRS="app tests"

# Function to run flake8
run_flake8() {
    info "Running flake8 linter"
    if flake8 $PROJECT_DIRS; then
        success "Flake8 passed"
    else
        error "Flake8 found issues"
        exit 1
    fi
}

# Function to run mypy
run_mypy() {
    info "Running mypy type checker"
    if mypy app --ignore-missing-imports; then
        success "MyPy passed"
    else
        error "MyPy found type issues"
        exit 1
    fi
}

# Main execution
step "Starting linting for FastAPI Chatbot"

run_flake8
run_mypy

success "All linting checks passed!"
