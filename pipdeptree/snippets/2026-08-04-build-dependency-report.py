# last_verified: 2026-08-04 · pipdeptree n/a
import json
import sys

# Load pipdeptree JSON from stdin
data = json.load(sys.stdin)

# Pick a package to report on — change this name to target a different package
target = "requests"

for pkg in data:
    if pkg["package"]["key"] == target:
        deps = pkg.get("dependencies", [])
        print(f"{target} dependencies:")
        for dep in deps:
            print(f"  - {dep['key']}=={dep['installed_version']}")
        break
else:
    print(f"{target} not found in pipdeptree output")