#!/usr/bin/env bash
# last_verified: 2026-07-23 · ruff latest

set -euo pipefail

PROJECT_DIR="$(mktemp -d)/sample_project"
mkdir -p "$PROJECT_DIR"

cat > "$PROJECT_DIR/main.py" <<'EOF'
import json, os

x = "hello"

def foo(a, b, c):
    result = a + b + c
    return result
EOF

cat > "$PROJECT_DIR/pyproject.toml" <<'EOF'
[project]
name = "sample"
version = "0.1.0"
EOF

echo "--- Sample project created at $PROJECT_DIR ---"
echo ""
echo "  main.py"
cat "$PROJECT_DIR/main.py"

echo ""
echo "=== ruff check (expect: F401 unused import, E501 line too long, etc.) ==="
ruff check "$PROJECT_DIR"

echo ""
echo "=== Applying ruff check --fix ==="
ruff check --fix "$PROJECT_DIR"

echo "  main.py after fix"
cat "$PROJECT_DIR/main.py"

echo ""
echo "=== ruff format --check ==="
if ruff format --check "$PROJECT_DIR" 2>/dev/null; then
    echo "  formatting ok"
else
    echo "  formatting issues found — applying ruff format"
    ruff format "$PROJECT_DIR"
    ruff format --check "$PROJECT_DIR"
fi

echo ""
echo "=== Final ruff check ==="
ruff check "$PROJECT_DIR" && echo "  all clear" || echo "  issues remain"

rm -rf "$(dirname "$PROJECT_DIR")"
