# last_verified: 2026-08-17 · pipdeptree n/a
#
# Reverse-dependency queries via the pipdeptree Python API.
# Builds a reverse lookup map from installed distributions.

import sys

try:
    import pipdeptree
except ImportError:
    print("pipdeptree not installed. Run: pip install pipdeptree", file=sys.stderr)
    sys.exit(1)

target = sys.argv[1] if len(sys.argv) > 1 else "requests"
target = target.lower()

distributions = list(pipdeptree.get_installed_distributions())
reverse_map: dict[str, list[str]] = {}

for dist in distributions:
    for req in dist.requires:
        dep_key = req.key
        reverse_map.setdefault(dep_key, []).append(dist.project_name)

dependents = reverse_map.get(target, [])
if dependents:
    print(f"Packages that depend on {target}:")
    for name in sorted(set(dependents)):
        print(f"  - {name}")
else:
    print(f"No installed packages depend on {target}.")
