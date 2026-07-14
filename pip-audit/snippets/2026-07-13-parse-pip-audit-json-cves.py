# last_verified: 2026-07-13 · pip-audit 2.10.1
#
# Pipe pip-audit JSON through this to list packages with CVEs.
# Usage: pip-audit --format json -r requirements.txt | python3 this-script.py

import json, sys

data = json.load(sys.stdin)
for dep in data.get("dependencies", []):
    for vuln in dep.get("vulnerabilities", []):
        cve = vuln.get("id", "?")
        sev = vuln.get("severity", "unknown")
        print(f"{dep['name']}=={dep['version']}  {cve}  severity={sev}")
