#!/usr/bin/env bash
# Create a minimal pyproject.toml by hand, then generate uv.lock and inspect it

TMPDIR=$(mktemp -d)
cd "$TMPDIR" || exit 1

cat > pyproject.toml << 'EOF'
[project]
name = "demo-inspect"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["requests", "click>=8.0"]
EOF

uv lock

echo "=== uv.lock generated ==="
echo "Lines: $(wc -l < uv.lock)"
echo "Packages: $(grep -c '^name' uv.lock)"
echo ""
echo "=== First 20 lines ==="
head -20 uv.lock

rm -rf "$TMPDIR"
