#!/usr/bin/env python3
# last_verified: 2026-09-03 · pipdeptree n/a

"""Dependency-health helper for pipdeptree.

Purpose
-------
Produce a JSON report that combines three views of a Python environment's
dependency graph: a JSON tree of installed packages, a triage of version
conflicts and missing dependencies, and a list of cyclic dependency chains.

When to use
-----------
- Before cutting a release to verify the dependency graph has no obvious
  version conflicts.
- In CI to fail fast when a new cyclic dependency is introduced.
- When auditing a project to understand which packages are top-level versus
  transitive.

Prerequisites
-------------
- ``pipdeptree`` installed in the environment being inspected.
- Python 3.8+ (uses ``json`` and ``collections`` from the standard library).

Steps
-----
1. Enumerate installed distributions via ``pipdeptree.get_installed_distributions()``.
2. Build a JSON tree rooted at top-level packages.
3. Walk the graph to detect cycles.
4. Compare each dependency's specifier against the installed version to
   surface conflicts and missing packages.
5. Print the combined report as JSON; exit non-zero if cycles are found.

Verify
------
Run the script in any virtual environment with installed packages::

    python pipdeptree/scripts/dependency-health-helper.py > report.json

A clean environment produces ``"cycles_found": 0``. Introduce a cycle
(e.g., ``pip install`` two packages that depend on each other) and the
script exits 1 with the cycle listed under ``"cycles"``.

Common errors
-------------
- **ImportError: No module named 'pipdeptree'** — install it first:
  ``pip install pipdeptree``.
- **RecursionError on very deep trees** — the tree builder uses recursion;
  environments with hundreds of nested transitive dependencies may hit the
  recursion limit. Increase it with ``sys.setrecursionlimit`` if needed.
- **False-positive version conflicts** — some packages report ``Arbitrary``
  or ``*`` specifiers; the script treats these as compatible.

References
----------
- pipdeptree is maintained by the tox-dev organization and is the standard
  tool for visualizing Python dependency trees.
"""

import json
import sys
from collections import defaultdict

try:
    import pipdeptree
except ImportError:
    print("pipdeptree is not installed. Run: pip install pipdeptree", file=sys.stderr)
    sys.exit(1)


def build_json_tree(packages):
    """Build a JSON-serializable dependency tree rooted at top-level packages."""
    pkg_map = {p.key: p for p in packages}
    children_map = defaultdict(list)
    for pkg in packages:
        for dep in pkg.requires:
            children_map[pkg.key].append(dep.key)

    def build(node_key, visiting):
        node = {
            "package": node_key,
            "version": pkg_map[node_key].version,
            "dependencies": [],
        }
        if node_key in visiting:
            node["cycle"] = True
            return node
        visiting.add(node_key)
        for child_key in children_map.get(node_key, []):
            node["dependencies"].append(build(child_key, visiting))
        visiting.discard(node_key)
        return node

    depended = set()
    for deps in children_map.values():
        depended.update(deps)
    roots = [p.key for p in packages if p.key not in depended]
    if not roots:
        roots = [packages[0].key] if packages else []

    return [build(root, set()) for root in roots]


def detect_cycles(packages):
    """Return a list of cyclic dependency chains."""
    children_map = defaultdict(list)
    for pkg in packages:
        for dep in pkg.requires:
            children_map[pkg.key].append(dep.key)

    cycles = []
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {p.key: WHITE for p in packages}
    path = []

    def dfs(node_key):
        color[node_key] = GRAY
        path.append(node_key)
        for child_key in children_map.get(node_key, []):
            child_color = color.get(child_key, WHITE)
            if child_color == GRAY:
                cycle_start = path.index(child_key)
                cycles.append(path[cycle_start:] + [child_key])
            elif child_color == WHITE:
                dfs(child_key)
        path.pop()
        color[node_key] = BLACK

    for pkg in packages:
        if color[pkg.key] == WHITE:
            dfs(pkg.key)

    return cycles


def triage_warnings(packages):
    """Identify version conflicts and missing dependencies."""
    pkg_map = {p.key: p for p in packages}
    warnings = []

    for pkg in packages:
        for dep in pkg.requires:
            installed = pkg_map.get(dep.key)
            if not installed:
                warnings.append({
                    "type": "missing_dependency",
                    "package": pkg.project_name,
                    "dependency": dep.key,
                    "required": str(dep.specifier) if dep.specifier else "any",
                })
                continue
            if dep.specifier and installed.version not in dep.specifier:
                warnings.append({
                    "type": "version_conflict",
                    "package": pkg.project_name,
                    "dependency": dep.key,
                    "required": str(dep.specifier),
                    "installed": installed.version,
                })

    return warnings


def main():
    try:
        packages = pipdeptree.get_installed_distributions()
    except Exception as exc:
        print(f"Failed to enumerate installed packages: {exc}", file=sys.stderr)
        sys.exit(1)

    if not packages:
        report = {
            "dependency_tree": [],
            "cycles": [],
            "warnings": [],
            "summary": {
                "total_packages": 0,
                "cycles_found": 0,
                "warnings_found": 0,
            },
        }
        print(json.dumps(report, indent=2))
        return

    tree = build_json_tree(packages)
    cycles = detect_cycles(packages)
    warnings = triage_warnings(packages)

    report = {
        "dependency_tree": tree,
        "cycles": cycles,
        "warnings": warnings,
        "summary": {
            "total_packages": len(packages),
            "cycles_found": len(cycles),
            "warnings_found": len(warnings),
        },
    }

    print(json.dumps(report, indent=2))

    if cycles:
        sys.exit(1)


if __name__ == "__main__":
    main()
