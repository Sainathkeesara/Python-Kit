#!/bin/bash
# Install pre-commit and run on my repo

uv pip install pre-commit
pre-commit install
echo "Running pre-commit on all files..."
pre-commit run --all-files