#!/usr/bin/env bash
# This script installs required development tools for FastAPI Chatbot.

set -e

# Source message handler functions
source "$(dirname "$0")/message-handler.sh"

# Function to install formatting tools
install_formatting_tools() {
    info "Installing formatting tools"
    pip install black isort autoflake
    success "Formatting tools installed"
}

# Function to install linting tools
install_linting_tools() {
    info "Installing linting tools"
    pip install flake8 mypy
    success "Linting tools installed"
}

# Function to install testing tools
install_testing_tools() {
    info "Installing testing tools"
    pip install pytest pytest-cov pytest-mock pytest-asyncio safety
    success "Testing tools installed"
}

# Function to install all tools
install_all_tools() {
    info "Installing all development tools"
    
    # Install from requirements if available
    if [[ -f "requirements-dev.txt" ]]; then
        info "Installing from requirements-dev.txt"
        pip install -r requirements-dev.txt
    else
        # Install individually
        install_formatting_tools
        install_linting_tools
        install_testing_tools
    fi
    
    # Install nox for session management
    pip install nox
    
    success "All development tools installed!"
}

# Main execution
step "Installing development tools for FastAPI Chatbot"

# Check if pip is available
if ! command -v pip &> /dev/null; then
    error "pip not found. Please install pip first."
    exit 1
fi

# Upgrade pip
info "Upgrading pip"
python -m pip install --upgrade pip

# Install tools
install_all_tools

info "Installation completed! You can now run:"
info "  ./run_local.sh -f    # Format code"
info "  ./run_local.sh -l    # Lint code"
info "  ./run_local.sh -t    # Run tests"
info "  ./run_local.sh -n    # Run nox"
