#!/bin/bash
# last_verified: 2026-07-17 · pre-commit 4.2.0
#
# Set up a sample Python project, configure pre-commit with ruff
# and trailing-whitespace hooks, then run the hooks once.
# Based on pre-commit L1/L2 research findings.

set -e

WORKDIR="$(mktemp -d)/sample-project"
mkdir -p "$WORKDIR/src"

cat > "$WORKDIR/.pre-commit-config.yaml" <<'YAML'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.0
    hooks:
      - id: ruff
      - id: ruff-format
YAML

cat > "$WORKDIR/pyproject.toml" <<'TOML'
[project]
name = "sample-project"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = []
TOML

cat > "$WORKDIR/src/main.py" <<'PY'
def greet(name: str) -> str:
    return f"Hello, {name}!"
PY

cd "$WORKDIR"
git init
git add .
git commit -m "initial"

pre-commit install
pre-commit run --all-files

echo "Done. Hooks passed in $WORKDIR"
