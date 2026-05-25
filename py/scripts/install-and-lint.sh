#!/bin/bash
# Install Ruff and lint a Python file

# Install ruff with uv
uv tool install ruff

# Create a test file to lint
cat > test_lint.py << 'EOF'
import os
def hello(  ):
    print("hello world")
EOF

# Run ruff on it
ruff check test_lint.py