# last_verified: 2026-07-05 · n/a

"""
Common packaging patterns I practiced — reading pyproject.toml
metadata and understanding how Python discovers packages.
I wanted something I could copy into future projects.
"""

import tomllib
from pathlib import Path


def read_project_metadata(path: str = "pyproject.toml") -> dict:
    """Parse PEP 621 project metadata from pyproject.toml.

    Had to open in 'rb' mode because tomllib expects bytes.
    """
    with open(path, "rb") as f:
        data = tomllib.load(f)
    project = data.get("project", {})
    return {
        "name": project.get("name", "unknown"),
        "version": project.get("version", "0.0.0"),
        "requires_python": project.get("requires-python", ">=3.8"),
        "dependencies": project.get("dependencies", []),
        "optional_dependencies": project.get("optional-dependencies", {}),
    }


def find_packages(root: str = ".") -> list[str]:
    """Find directories that look like Python packages (contain __init__.py)."""
    packages = []
    for p in Path(root).iterdir():
        if p.is_dir() and (p / "__init__.py").exists():
            packages.append(p.name)
    return packages


if __name__ == "__main__":
    meta = read_project_metadata()
    print(f"Package: {meta['name']} v{meta['version']}")
    print(f"Requires Python: {meta['requires_python']}")
    print(f"Dependencies ({len(meta['dependencies'])}):")
    for dep in meta['dependencies']:
        print(f"  - {dep}")
    discovered = find_packages()
    if discovered:
        print(f"Discovered packages: {discovered}")
