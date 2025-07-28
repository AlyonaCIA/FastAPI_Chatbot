#!/usr/bin/env bash
# This script performs in-place formatting of Python files for FastAPI Chatbot.

set -e

# Source message handler functions
source "$(dirname "$0")/message-handler.sh"

# Configuration
PROJECT_DIRS="app tests"

# Function to check if a command exists
check_command() {
    if ! command -v $1 &> /dev/null; then
        error "$1 could not be found. Please install it: pip install $1"
        exit 1
    fi
}

# Main script
step "Starting code formatting for FastAPI Chatbot"

# Check necessary commands
check_command black
check_command isort

info "Sorting imports with isort"
isort $PROJECT_DIRS

info "Formatting code with black"
black $PROJECT_DIRS

success "Code formatting completed!"
