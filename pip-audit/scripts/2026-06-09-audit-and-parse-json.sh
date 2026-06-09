#!/usr/bin/env bash
# Run pip-audit on a requirements.txt with known-CVE entries and parse JSON output

pip install pip-audit

pip-audit --requirement requirements.txt --local --format json > /tmp/audit-results.json || true

jq -r '.[] | "- \(.package): fix in \(.fix_versions[0])" ' /tmp/audit-results.json
