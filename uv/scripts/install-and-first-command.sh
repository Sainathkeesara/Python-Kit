#!/usr/bin/env bash
# Install uv and run my first command
# Based on the official installer at https://docs.astral.sh/uv/

set -e  # stop if anything fails

echo "--- Installing uv ---"
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "--- Checking version ---"
uv --version

echo "--- Listing available Python versions ---"
uv python list
