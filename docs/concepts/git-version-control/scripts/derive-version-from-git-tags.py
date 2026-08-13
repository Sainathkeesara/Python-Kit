# last_verified: 2026-08-12 · Git Version Control n/a

"""Derive a package version from git tags, setuptools-scm style.

Pure-stdlib take on the version-from-tags pattern that tools like
setuptools-scm implement: walk back to the nearest reachable tag, count
commits since it, and append the short commit hash for anything that is
not exactly on a tag. The result is close to PEP 440 so package managers
can compare versions from a plain git history without a version file.

Usage: python derive-version-from-git-tags.py [path-to-repo]
"""

import re
import subprocess
import sys
from pathlib import Path

TAG_RE = re.compile(r"^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?$")


def run_git(args, cwd):
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def parse_tag(tag):
    match = TAG_RE.match(tag)
    if not match:
        return None
    parts = [int(p) for p in match.groups() if p is not None]
    return (parts + [0] * (3 - len(parts)))


def version_from_git(repo_root):
    root = str(repo_root)
    short_hash = run_git(["rev-parse", "--short=7", "HEAD"], root)

    try:
        tag = run_git(["describe", "--tags", "--abbrev=0"], root)
    except RuntimeError:
        distance = int(run_git(["rev-list", "--count", "HEAD"], root))
        return f"0.0.0.dev{distance}+g{short_hash}"

    counts = run_git(["rev-list", "--count", f"{tag}..HEAD"], root)
    distance = int(counts)
    parsed = parse_tag(tag)
    if parsed is None:
        return f"0.0.0.dev{distance}+g{short_hash}"
    base = ".".join(str(p) for p in parsed)

    if distance == 0:
        return base
    return f"{base}.dev{distance}+g{short_hash}"


def main():
    repo_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    print(version_from_git(repo_root))


if __name__ == "__main__":
    main()
