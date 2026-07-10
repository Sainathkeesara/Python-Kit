# last_verified: 2026-07-10 · pip-audit 2.10.1
#
# Piping pip-audit's JSON output through this script to see
# which packages have CVEs and how bad they are.
#
# Usage:
#   pip-audit --format json -r requirements.txt | python3 this-script.py

import json, sys

data = json.load(sys.stdin)
for dep in data.get("dependencies", []):
    for vuln in dep.get("vulnerabilities", []):
        cve = vuln.get("id", "?")
        sev = vuln.get("severity", "unknown")
        print(f"{dep['name']}=={dep['version']}  {cve}  severity={sev}")
