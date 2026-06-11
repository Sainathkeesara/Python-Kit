#!/usr/bin/env bash
# Bootstrap a one-file Python script with uv run and external deps

mkdir -p /tmp/uv-bootstrap-demo

cat > /tmp/uv-bootstrap-demo/hello.py << 'PYEOF'
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
# ]
# ///

import requests

resp = requests.get("https://api.github.com")
print(f"GitHub API status: {resp.status_code}")
PYEOF

echo "--- Running the script with uv run ---"
uv run /tmp/uv-bootstrap-demo/hello.py
