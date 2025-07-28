#!/usr/bin/env bash
# This script checks the formatting of Python files in FastAPI Chatbot.

set -e

# Source message handler functions
source "$(dirname "$0")/message-handler.sh"

# Configuration for this project
PROJECT_DIRS="app tests"

# Function to get all Python files
get_python_files() {
    find $PROJECT_DIRS -name "*.py" -type f 2>/dev/null || echo ""
}

# Function to check formatting with black
check_black() {
    info "Checking formatting with black"
    files=$(get_python_files)
    if [[ -z "$files" ]]; then
        warning "No Python files found"
        return 0
    fi
    
    echo "Processing files: $files"
    if black --check --diff $files; then
        success "Black formatting check passed!"
    else
        error "Black formatting check failed - run 'black $PROJECT_DIRS' to fix"
        exit 2
    fi
}

# Function to check import sorting with isort
check_isort() {
    info "Checking import sorting with isort"
    files=$(get_python_files)
    if [[ -z "$files" ]]; then
        warning "No Python files found"
        return 0
    fi
    
    echo "Processing files: $files"
    if isort --check-only --diff $files; then
        success "isort check passed!"
    else
        error "isort check failed - run 'isort $PROJECT_DIRS' to fix"
        exit 2
    fi
}

# Function to check with flake8 (basic style)
check_flake8_style() {
    info "Checking basic style with flake8"
    if flake8 $PROJECT_DIRS; then
        success "Flake8 style check passed!"
    else
        error "Flake8 style check failed"
        exit 2
    fi
}

# Function to check for unused imports (optional)
check_unused_imports() {
    info "Checking for unused imports"
    
    # Only check if autoflake is available
    if ! command -v autoflake &> /dev/null; then
        warning "autoflake not found, skipping unused import check"
        return 0
    fi
    
    files=$(get_python_files)
    if [[ -z "$files" ]]; then
        warning "No Python files found"
        return 0
    fi
    
    if autoflake \
        --check \
        --remove-all-unused-imports \
        --ignore-init-module-imports \
        --exclude=__pycache__ \
        $files; then
        success "No unused imports found!"
    else
        warning "Unused imports found (non-blocking)"
        info "Run 'autoflake --in-place --remove-all-unused-imports $files' to fix"
    fi
}

# Main script
step "Starting formatting validation for FastAPI Chatbot"

# Check if tools are available
missing_tools=()

if ! command -v black &> /dev/null; then
    missing_tools+=("black")
fi

if ! command -v isort &> /dev/null; then
    missing_tools+=("isort")
fi

if ! command -v flake8 &> /dev/null; then
    missing_tools+=("flake8")
fi

if [[ ${#missing_tools[@]} -gt 0 ]]; then
    error "Missing required tools: ${missing_tools[*]}"
    info "Install with: pip install ${missing_tools[*]}"
    exit 1
fi

# Run checks
check_black
check_isort
check_flake8_style
check_unused_imports

success "All formatting checks passed! ✓"
