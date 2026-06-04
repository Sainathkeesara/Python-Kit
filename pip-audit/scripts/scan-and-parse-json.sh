#!/bin/bash
# Scan requirements.txt with pip-audit and parse JSON output

# Generate a requirements.txt for testing
uv pip freeze > /tmp/requirements.txt

# Scan and save JSON output
pip-audit --requirement /tmp/requirements.txt --format json > /tmp/audit.json

# Print a summary using jq (parse JSON)
if [ -f /tmp/audit.json ] && [ -s /tmp/audit.json ]; then
    echo "=== Vulnerabilities found ==="
    jq -r '.vulnerabilities[] | "\(.package) \(.version) — \(.aliases[0] // .id)"' /tmp/audit.json 2>/dev/null || echo "No vulnerabilities or jq not installed"
    echo "=== Raw JSON ==="
    cat /tmp/audit.json
else
    echo "No vulnerabilities found."
fi
