#!/bin/bash
# Install pipdeptree and inspect the /work project's dependency tree

set -e

pip install pipdeptree

cd /work

echo "=== pipdeptree default output ==="
pipdeptree

echo ""
echo "=== pipdeptree JSON output ==="
pipdeptree --json