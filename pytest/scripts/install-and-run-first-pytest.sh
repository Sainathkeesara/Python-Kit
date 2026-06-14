#!/usr/bin/env bash
# Install pytest and run my first passing test

# Install pytest if not already installed
uv pip install pytest --quiet 2>/dev/null || pip install pytest --quiet

# Create a minimal test file
cat > test_pass.py << 'EOF'
def test_always_passes():
    assert 1 + 1 == 2
EOF

echo "Running first test with python -m pytest..."
python -m pytest test_pass.py -v

rm test_pass.py
echo "Done."