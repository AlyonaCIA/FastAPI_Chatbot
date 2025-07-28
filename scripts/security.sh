#!/usr/bin/env bash
# This script runs security audits on the Python codebase.

set -e

# Source message handler functions
source ./ci/scripts/message-handler.sh

# Ensure required tools are installed
pip install -r ci/requirements/audit.txt

# Function to check if command exists
check_command() {
    if ! command -v $1 &> /dev/null; then
        error "$1 could not be found. Installing..."
        return 1
    fi
    return 0
}

# Function to setup test environment
setup_test_environment() {
    info "Setting up test environment"

    # Create necessary directories
    mkdir -p junit
    mkdir -p htmlcov

    # Install package in editable mode if not already done
    info "Installing featlib in editable mode"
    pip install -e .

    # Configure Java for PySpark if available
    if command -v java &> /dev/null; then
        export JAVA_HOME=${JAVA_HOME:-$(dirname $(dirname $(readlink -f $(which java))))}
        info "Java found at: $JAVA_HOME"
    else
        warning "Java not found - PySpark tests may fail"
    fi
}

# Function to run pytest tests
run_pytest() {
    info "Running pytest unit tests"

    # Run tests with comprehensive options
    pytest tests/ \
        --verbose \
        --tb=short \
        --strict-markers \
        --strict-config \
        --cov=featlib \
        --cov-branch \
        --cov-report=term-missing:skip-covered \
        --cov-report=html:htmlcov \
        --cov-report=xml:coverage.xml \
        --junitxml=junit/test-results.xml \
        --cov-fail-under=80

    local test_exit_code=$?

    if [ $test_exit_code -eq 0 ]; then
        info "All tests passed!"

        # Display coverage summary
        if [ -f "coverage.xml" ]; then
            info "Coverage report generated in htmlcov/"
        fi

    else
        error "Some tests failed"
        info "Check junit/test-results.xml for detailed results"
        exit 1
    fi
}

# Function to run quick security check
run_quick_security_check() {
    info "Running quick security check"

    # This is a lightweight check, main security audit is in separate stage
    if command -v pip-audit &> /dev/null; then
        pip-audit --format=text --desc || {
            warning "Security issues found (non-blocking in test stage)"
            info "Check Security Audit stage for detailed analysis"
        }
    else
        warning "pip-audit not available, skipping quick security check"
    fi
}

# Function to validate test results
validate_test_results() {
    info "Validating test results"

    # Check if junit results exist
    if [ ! -f "junit/test-results.xml" ]; then
        error "JUnit test results not found"
        exit 1
    fi

    # Check if coverage report exists
    if [ ! -f "coverage.xml" ]; then
        warning "Coverage report not found"
    fi

    # Display test summary
    if command -v python &> /dev/null; then
        python -c "
import xml.etree.ElementTree as ET
try:
    tree = ET.parse('junit/test-results.xml')
    root = tree.getroot()
    tests = root.get('tests', '0')
    failures = root.get('failures', '0')
    errors = root.get('errors', '0')
    time = root.get('time', '0')

    print(f'Test Summary:')
    print(f'   Total tests: {tests}')
    print(f'   Failures: {failures}')
    print(f'   Errors: {errors}')
    print(f'   Duration: {float(time):.2f}s')

    if int(failures) == 0 and int(errors) == 0:
        print('   Status: ALL TESTS PASSED')
    else:
        print('   Status: SOME TESTS FAILED')

except Exception as e:
    print(f'Could not parse test results: {e}')
"
    fi
}

# Main execution
info "Starting comprehensive test execution for featlib"

# Setup
setup_test_environment

# Run tests
run_pytest

# Quick security check (non-blocking)
run_quick_security_check

# Validate results
validate_test_results

info "Test execution completed successfully! :)"
info "Reports available:"
info "  - JUnit: junit/test-results.xml"
info "  - Coverage HTML: htmlcov/index.html"
info "  - Coverage XML: coverage.xml"¨
