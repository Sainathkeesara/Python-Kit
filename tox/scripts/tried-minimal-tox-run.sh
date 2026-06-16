#!/usr/bin/env bash
# Minimal tox.ini with a test env, run it end-to-end
# I wanted to see tox create a venv, install deps, and run tests from scratch.

tmpdir=$(mktemp -d)
cd "$tmpdir" || exit

cat > tox.ini <<'EOF'
[tox]
envlist = py311

[testenv]
skip_install = true
deps = pytest
commands = python -m pytest
EOF

cat > test_example.py <<'EOF'
def test_ok():
    assert 1 + 1 == 2
EOF

tox

echo "--- tox ran, exit code $? ---"
rm -rf "$tmpdir"
