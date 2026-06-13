"""Parse uv.lock and look for packages with conflicting version constraints."""

import tomllib
from collections import defaultdict

with open("uv.lock", "rb") as f:
    data = tomllib.load(f)

constraints = defaultdict(list)

for pkg in data.get("package", []):
    name = pkg["name"]
    for req in pkg.get("requirements", []):
        dep_name = req.get("name", "?")
        constraint = req.get("version", req.get("specifier", "*"))
        constraints[dep_name].append((name, constraint))

found = False
for dep_name, reqs in sorted(constraints.items()):
    vals = set(c for _, c in reqs)
    if len(vals) > 1:
        print(f"Conflict: {dep_name}")
        for src, c in reqs:
            print(f"  required by {src} as {c}")
        found = True

if not found:
    print("No version conflicts detected in uv.lock")
