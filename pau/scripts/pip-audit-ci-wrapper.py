#!/usr/bin/env python3
# last_verified: 2026-09-10 · pip-audit 2.10.1
#
# Reusable pip-audit CI wrapper: JSON output, vulnerability filtering,
# and exit-code mapping for GitHub Actions.
#
# Usage:
#   python pip-audit-ci-wrapper.py [options]
#
# Exit codes:
#   0 - no vulnerabilities found (or all below threshold)
#   1 - vulnerabilities found at or above threshold
#   2 - pip-audit error (not installed, scan failed)

import argparse
import json
import subprocess
import sys
from typing import NoReturn

SEVERITY_ORDER = {"low": 0, "medium": 1, "high": 2, "critical": 3}


def run_pip_audit(
    requirements: str | None = None,
    extras: list[str] | None = None,
) -> dict:
    """Run pip-audit and return parsed JSON output."""
    cmd = [sys.executable, "-m", "pip_audit", "--format", "json", "--strict"]
    if requirements:
        cmd.extend(["--requirement", requirements])
    if extras:
        cmd.extend(extras)

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode not in (0, 1):
        print(f"pip-audit failed (exit {result.returncode}): {result.stderr}", file=sys.stderr)
        sys.exit(2)

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"Failed to parse pip-audit JSON output: {result.stdout[:200]}", file=sys.stderr)
        sys.exit(2)


def filter_by_severity(vulns: list[dict], min_severity: str) -> list[dict]:
    """Keep only vulnerabilities at or above the given severity level."""
    threshold = SEVERITY_ORDER.get(min_severity, 0)
    filtered = []
    for v in vulns:
        sev = v.get("vulns", [{}])[0].get("severity", "low") if v.get("vulns") else "low"
        if SEVERITY_ORDER.get(sev, 0) >= threshold:
            filtered.append(v)
    return filtered


def format_github_summary(vulns: list[dict]) -> str:
    """Format vulnerabilities as a GitHub Actions job summary."""
    if not vulns:
        return "## No vulnerabilities found\n"

    lines = [f"## {len(vulns)} vulnerabilities found\n"]
    lines.append("| Package | Version | Vulnerability | Severity |")
    lines.append("|---------|---------|---------------|----------|")
    for v in vulns:
        pkg = v.get("name", "?")
        ver = v.get("version", "?")
        for vuln in v.get("vulns", []):
            vid = vuln.get("id", "?")
            sev = vuln.get("severity", "?")
            lines.append(f"| {pkg} | {ver} | {vid} | {sev} |")
    return "\n".join(lines) + "\n"


def main() -> NoReturn:
    parser = argparse.ArgumentParser(description="pip-audit CI wrapper with severity filtering")
    parser.add_argument("-r", "--requirement", help="Path to requirements/lockfile")
    parser.add_argument(
        "--min-severity",
        choices=["low", "medium", "high", "critical"],
        default="medium",
        help="Minimum severity to report (default: medium)",
    )
    parser.add_argument("--summary", action="store_true", help="Output GitHub Actions job summary")
    parser.add_argument("extras", nargs="*", help="Extra arguments passed to pip-audit")
    args = parser.parse_args()

    data = run_pip_audit(requirements=args.requirement, extras=args.extras)
    dependencies = data.get("dependencies", [])

    filtered = filter_by_severity(dependencies, args.min_severity)

    if args.summary:
        summary = format_github_summary(filtered)
        summary_file = "${GITHUB_STEP_SUMMARY}"
        if summary_file.startswith("$"):
            # Not in GitHub Actions — print to stdout instead
            print(summary)
        else:
            with open(summary_file, "a") as f:
                f.write(summary)

    if filtered:
        print(f"\n{len(filtered)} vulnerabilities at or above {args.min_severity} severity:")
        for v in filtered:
            pkg = v.get("name", "?")
            ver = v.get("version", "?")
            for vuln in v.get("vulns", []):
                vid = vuln.get("id", "?")
                sev = vuln.get("severity", "?")
                print(f"  {pkg} {ver}: {vid} ({sev})")
        sys.exit(1)
    else:
        print(f"No vulnerabilities at or above {args.min_severity} severity.")
        sys.exit(0)


if __name__ == "__main__":
    main()
