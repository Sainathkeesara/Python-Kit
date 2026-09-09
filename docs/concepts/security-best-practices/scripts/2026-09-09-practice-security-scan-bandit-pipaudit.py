# last_verified: 2026-09-09 · Security Best Practices (concept) · bandit 1.9.4
# I practiced security scanning on a deliberately vulnerable sample project:
# bandit for static source checks, pip-audit for dependency CVEs, combined
# into one script that exits non-zero when either tool reports findings.

import json
import shutil
import subprocess
import sys
from pathlib import Path


def has(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout


def main() -> int:
    if not has("bandit") or not has("pip-audit"):
        print("missing bandit or pip-audit — install both before running")
        return 2

    # 1. Static source scan with bandit, JSON output, high severity only.
    rc, out = run(["bandit", "-r", "sample_project", "-f", "json", "-lll"])
    if rc not in (0, 1):
        print(f"bandit failed to run (exit {rc})")
        return 2
    findings = json.loads(out).get("results", [])
    high = [f for f in findings if f.get("issue_severity") == "HIGH"]
    print(f"bandit: {len(findings)} findings, {len(high)} high severity")

    # 2. Dependency scan with pip-audit, JSON output.
    rc, out = run(["pip-audit", "-f", "json"])
    if rc not in (0, 1):
        print(f"pip-audit failed to run (exit {rc})")
        return 2
    vulns = json.loads(out).get("dependencies", [])
    vulns = [d for d in vulns if d.get("vulns")]
    print(f"pip-audit: {len(vulns)} vulnerable dependencies")

    if high or vulns:
        print("security gate FAILED")
        return 1
    print("security gate PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())