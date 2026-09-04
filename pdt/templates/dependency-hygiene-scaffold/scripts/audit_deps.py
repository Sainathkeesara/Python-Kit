#!/usr/bin/env python3
# last_verified: 2026-09-04 · pipdeptree n/a
#
# Analyze the dependency graph with pipdeptree and report on conflicts,
# cyclic dependencies, and reverse-dependency hotspots.
# Prints a JSON report to stdout. Exits 1 if cycles are found.

import json
import sys
from collections import defaultdict, Counter

try:
    import pipdeptree
except ImportError:
    print(
        "pipdeptree is not installed. "
        "Run: uv pip install pipdeptree",
        file=sys.stderr,
    )
    sys.exit(1)


def build_tree(packages: list) -> list:
    """Build a JSON-serializable tree rooted at top-level packages."""
    pkg_map = {p.key: p for p in packages}
    children = defaultdict(list)
    for pkg in packages:
        for dep in pkg.requires:
            children[pkg.key].append(dep.key)

    def _build(key: str, visiting: set) -> dict:
        node = {"package": key, "version": pkg_map[key].version, "dependencies": []}
        if key in visiting:
            node["cycle"] = True
            return node
        visiting.add(key)
        for child_key in children.get(key, []):
            node["dependencies"].append(_build(child_key, visiting))
        visiting.discard(key)
        return node

    depended = {d for deps in children.values() for d in deps}
    roots = [p.key for p in packages if p.key not in depended]
    if not roots and packages:
        roots = [packages[0].key]

    return [_build(root, set()) for root in roots]


def detect_cycles(packages: list) -> list:
    """Return a list of cyclic dependency chains."""
    children = defaultdict(list)
    for pkg in packages:
        for dep in pkg.requires:
            children[pkg.key].append(dep.key)

    cycles = []
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {p.key: WHITE for p in packages}
    path: list = []

    def dfs(key: str) -> None:
        color[key] = GRAY
        path.append(key)
        for child_key in children.get(key, []):
            child_color = color.get(child_key, WHITE)
            if child_color == GRAY:
                cycles.append(path[path.index(child_key) :] + [child_key])
            elif child_color == WHITE:
                dfs(child_key)
        path.pop()
        color[key] = BLACK

    for pkg in packages:
        if color[pkg.key] == WHITE:
            dfs(pkg.key)

    return cycles


def triage(packages: list) -> list:
    """Find version conflicts and missing dependencies."""
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


def main() -> None:
    try:
        packages = pipdeptree.get_installed_distributions()
    except Exception as exc:
        print(f"Failed to enumerate packages: {exc}", file=sys.stderr)
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

    tree = build_tree(packages)
    cycles = detect_cycles(packages)
    warnings = triage(packages)

    reverse_deps = Counter()
    for pkg in packages:
        for dep in pkg.requires:
            reverse_deps[dep.key] += 1

    top_10 = reverse_deps.most_common(10)

    report = {
        "dependency_tree": tree,
        "cycles": cycles,
        "warnings": warnings,
        "top_reverse_dependencies": [{"key": k, "count": c} for k, c in top_10],
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
