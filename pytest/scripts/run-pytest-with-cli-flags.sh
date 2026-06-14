#!/usr/bin/env bash
# Create a test file and run pytest with common CLI flags

# Create a simple test file
cat > test_sample.py << 'EOF'
def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 0) == 0
EOF

echo "Test file created. Running pytest with -v, -k add, -x, --tb=short..."
pytest -v -k add -x --tb=short test_sample.py

rm test_sample.py