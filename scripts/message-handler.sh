#!/usr/bin/env bash
# This script provides functions for handling messages
# with colored output in the terminal.

# Check if tput is available
if ! command -v tput &> /dev/null; then
    echo "[ERROR] tput not found, colors and styles won't be applied."
    exit 1
fi

export TERM=xterm-256color

# Define ANSI escape codes for colors and styles
bold=$(tput bold)
red=$(tput setaf 1)
green=$(tput setaf 2)
yellow=$(tput setaf 3)
reset=$(tput sgr0)

# Function to print messages with specified color
print_message() {
    local color=$1
    local type=$2
    local message=$3
    echo -e "${bold}${color}[${type}]${reset} ${message}"
}

# Function to print info message
info() {
    echo -e "${bold}${green}[INFO]${reset} $1"
}

# Function to print warning message
warning() {
    echo -e "${bold}${yellow}[WARNING]${reset} $1"
}

# Function to print error message
error() {
    echo -e "${bold}${red}[ERROR]${reset} $1" >&2
}
