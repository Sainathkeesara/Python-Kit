# last_verified: 2026-08-05 · tox n/a
pip install tox

cat > tox.ini <<'EOF'
[tox]
envlist = py311
[testenv]
deps = pytest
commands = python -m pytest
EOF

cat > test_example.py <<'EOF'
def test_ok():
    assert 1 + 1 == 2
EOF

tox