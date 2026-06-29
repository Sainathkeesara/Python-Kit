# tried-list-cves.py — run pip-audit JSON through this to see what's vulnerable
# TODO: not sure why --quiet doesn't suppress the pip-audit header yet
import json
import sys

data = json.load(sys.stdin)
for finding in data:
    pkg = finding.get("package", "?")
    ver = finding.get("version", "?")
    cve = finding.get("id", "?")
    sev = finding.get("severity", "unknown")
    print(f"{pkg}=={ver}  {cve}  severity={sev}")
