#!/bin/bash

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed or not in the PATH."
    exit 1
fi

# Get Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)
MINOR=$(echo "$PYTHON_VERSION" | cut -d. -f2)

# Check if Python version is 3.11 or newer
if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 11 ]); then
    echo "Error: Python 3.11 or newer is required. Detected version: $PYTHON_VERSION."
    exit 1
fi

# Create the virtual environment in .venv
echo "Creating virtual environment in .venv..."
python -m venv .venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create the virtual environment."
    exit 1
fi
./.venv/Scripts/pip install -r requirements.txt  # TODO: This needs to be checked!

echo "Virtual environment created successfully in .venv."
exit 0
