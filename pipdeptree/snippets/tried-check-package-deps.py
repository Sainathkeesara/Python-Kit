# Minimal script to check pipdeptree for a specific package and show its deps
# Usage: python tried-check-package-deps.py <package-name>

import json
import subprocess
import sys

target = sys.argv[1].lower()

# Ran pipdeptree --json and parsed it — took me a minute to figure out
# the JSON structure: list of objects, each with "package" and "dependencies"
data = json.loads(
    subprocess.check_output(["pipdeptree", "--json"], text=True)
)

entry = next(
    (p for p in data if p["package"]["key"].lower() == target), None
)

if not entry:
    print(f"{target}: not found")
    sys.exit(1)

# Walk the dependency chain recursively
stack = [(entry, 0)]
while stack:
    item, depth = stack.pop()
    pkg = item["package"]
    ver = pkg.get("installed_version", "?")
    print(f"{'  ' * depth}{pkg['key']}=={ver}")
    # Not sure if this handles circular deps correctly — pipdeptree should
    # already have resolved them though
    stack.extend((d, depth + 1) for d in item.get("dependencies", []))
