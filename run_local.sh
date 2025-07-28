#!/usr/bin/env bash

# Local development script for FastAPI Chatbot
# This script provides a convenient way to set up the local development environment,
# run tests, format code, and manage dependencies using nox.

set -e

# Configuration
export PYTHON_VERSION="3.11"
export PROJECT_NAME="FastAPI Chatbot"

# Initialize flags
run_format=false
run_test=false
run_install=false
run_nox=false
run_clean=false
run_lint=false
verbose=false

function info {
    echo -e "\033[1;34m[INFO]\033[0m $1"
}

function warning {
    echo -e "\033[1;33m[WARNING]\033[0m $1"
}

function error {
    echo -e "\033[1;31m[ERROR]\033[0m $1"
}

function success {
    echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}

function print_usage {
cat << EOF
    Local Development Script for FastAPI Chatbot
    
    USAGE:
        ./run_local.sh [OPTIONS]

    OPTIONS:
        -i, --install       Initialize environment and install dependencies
        -f, --format        Run code formatting (black, isort)
        -l, --lint          Run linting (flake8, mypy)
        -t, --test          Run tests with pytest
        -n, --nox           Use nox (recommended - mirrors CI exactly)
        -c, --clean         Clean up generated files and caches
        -v, --verbose       Enable verbose output
        -h, --help          Show this help

    EXAMPLES:
        ./run_local.sh -i           # Initialize environment
        ./run_local.sh -f           # Format code
        ./run_local.sh -l           # Run linting
        ./run_local.sh -t           # Run tests
        ./run_local.sh -n           # Run all nox sessions
        ./run_local.sh -c           # Clean up
EOF
}

function check_environment {
    info "Checking environment for $PROJECT_NAME"
    
    if command -v python3 &> /dev/null; then
        local current_version=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
        if [[ "$current_version" != "$PYTHON_VERSION" ]]; then
            warning "Python $current_version detected, $PYTHON_VERSION recommended"
        else
            info "Using Python $current_version ✓"
        fi
    else
        error "Python 3 not found, please install Python $PYTHON_VERSION"
        exit 1
    fi

    if [[ -z "${VIRTUAL_ENV:-}" ]] && [[ -z "${CONDA_DEFAULT_ENV:-}" ]]; then
        warning "No virtual environment detected"
        info "It's recommended to use a virtual environment"
    else
        info "Virtual environment detected ✓"
    fi
}

function initialize_environment {
    info "Initializing development environment"

    python -m pip install --upgrade pip

    if [[ -f "requirements.txt" ]]; then
        info "Installing main requirements"
        pip install -r requirements.txt
    fi

    if [[ -f "requirements-dev.txt" ]]; then
        info "Installing development requirements"
        pip install -r requirements-dev.txt
    fi

    info "Installing nox"
    pip install nox

    success "Environment initialization completed"
}

function run_format {
    info "Running code formatting"
    if command -v nox &> /dev/null; then
        nox -s format
    else
        black app/ tests/
        isort app/ tests/
    fi
}

function run_lint {
    info "Running code linting"
    if command -v nox &> /dev/null; then
        nox -s lint
    else
        flake8 app/
        mypy app/
    fi
}

function run_tests {
    info "Running tests"
    if command -v nox &> /dev/null; then
        nox -s tests
    else
        pytest
    fi
}

function run_nox {
    info "Running nox (mirrors CI pipeline)"

    if ! command -v nox &> /dev/null; then
        error "Nox not found. Run: ./run_local.sh -i"
        exit 1
    fi

    if [[ "$verbose" == "true" ]]; then
        nox -v
    else
        nox
    fi
}

function clean_files {
    info "Cleaning up generated files and caches"

    rm -rf .pytest_cache htmlcov .coverage __pycache__ .nox .mypy_cache
    find . -name "*.pyc" -delete 2>/dev/null || true
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
    find . -name "*.egg-info" -type d -exec rm -rf {} + 2>/dev/null || true
    rm -rf build/ dist/ 2>/dev/null || true

    success "Cleanup completed"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--format)
            run_format=true
            shift
            ;;
        -l|--lint)
            run_lint=true
            shift
            ;;
        -t|--test)
            run_test=true
            shift
            ;;
        -i|--install)
            run_install=true
            shift
            ;;
        -n|--nox)
            run_nox=true
            shift
            ;;
        -c|--clean)
            run_clean=true
            shift
            ;;
        -v|--verbose)
            verbose=true
            shift
            ;;
        -h|--help)
            print_usage
            exit 0
            ;;
        *)
            error "Unknown option: $1"
            print_usage
            exit 1
            ;;
    esac
done

# Main execution
function main {
    info "Starting $PROJECT_NAME development workflow"

    check_environment

    if [[ "$run_install" == "true" ]]; then
        initialize_environment
        exit 0
    fi

    if [[ "$run_nox" == "true" ]]; then
        run_nox
        exit 0
    fi

    if [[ "$run_clean" == "true" ]]; then
        clean_files
        exit 0
    fi

    if [[ "$run_format" == "true" ]]; then
        run_format
    fi

    if [[ "$run_lint" == "true" ]]; then
        run_lint
    fi

    if [[ "$run_test" == "true" ]]; then
        run_tests
    fi

    if [[ "$run_format" == "false" && "$run_lint" == "false" && "$run_test" == "false" ]]; then
        print_usage
    fi
}

main "$@"
function check_formatting {
    info "Checking code formatting"
    if command -v nox &> /dev/null; then
        nox -s format -- --check
    else
        bash scripts/validate_formatting.sh
    fi
}
