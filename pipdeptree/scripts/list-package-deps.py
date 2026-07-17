#!/usr/bin/env python3
# last_verified: 2026-07-17 · pipdeptree n/a
#
# List all dependencies of a named package using pipdeptree as a library.
# Usage: python3 list-package-deps.py <package-name>

import sys
import json

try:
    import pipdeptree
except ImportError:
    print("pipdeptree not installed. Run: pip install pipdeptree", file=sys.stderr)
    sys.exit(1)

pkg_name = sys.argv[1] if len(sys.argv) > 1 else None
if not pkg_name:
    print("Usage: list-package-deps.py <package-name>", file=sys.stderr)
    sys.exit(1)

pkgs = {p.key: p for p in pipdeptree.get_installed_distributions()}
target = pkgs.get(pkg_name.lower())
if not target:
    print(f"Package '{pkg_name}' not found in environment.", file=sys.stderr)
    sys.exit(1)

print(f"Dependencies of {target.project_name}=={target.version}:\n")
for dep in target.requires:
    name = dep.key
    specs = ", ".join(f"{s.operator}{s.version}" for s in dep.specifier)
    print(f"  {name} {specs}")
