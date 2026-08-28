# last_verified: 2026-08-28 · Security Best Practices concept (n/a version)

"""
I wrote this to practice three security habits the concept research kept
highlighting: checking my dependencies for known issues, not leaking
secrets into source or logs, and never deserializing untrusted data with
naive parsers. Each section is small and runnable so I can see it work.

Habit 1 - dependency scanning: run a vulnerability scanner over the
installed packages and treat a non-zero exit as a finding to fix, not a
warning to shrug at. pip-audit is the scanner I reach for.

Habit 2 - secrets detection: scan a string/blob for anything that looks
like a hardcoded secret (API key, private key block, password=...) so it
gets flagged before it lands in a repo or a log.

Habit 3 - safe deserialization: the research called out that parsing
untrusted XML with etree / xmlrpc enables billion-laughs and XXE attacks.
The fix is a hardened parser (defusedxml) or explicit schema checking.
"""

import os
import re
import subprocess
import sys

# ---------------------------------------------------------------------------
# Habit 1: dependency scanning with pip-audit
# ---------------------------------------------------------------------------

def scan_dependencies() -> None:
    """Gate on known issues in installed dependencies.

    I keep this as a thin wrapper so a project can call it in CI like any
    other step. pip-audit reports vulnerabilities in the installed package
    set; a non-zero exit means something is actionable, and I fail the build
    rather than proceeding. No flags are invented here beyond the bare
    command - the exit code is what carries the signal.
    """
    try:
        result = subprocess.run(
            ["pip-audit"],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        print("scan_dependencies: pip-audit is not installed - install it first.")
        return
    print(result.stdout or result.stderr)
    if result.returncode != 0:
        print(f"scan_dependencies: found actionable findings (exit {result.returncode}).")
        sys.exit(result.returncode)
    print("scan_dependencies: no known issues found.")


# ---------------------------------------------------------------------------
# Habit 2: secrets detection
# ---------------------------------------------------------------------------

# A private key reveals itself by its header/footer - no way to confuse it
# with a normal string. API keys often follow token= or key= and a long
# opaque value. I look for both to catch the common leak shapes the
# research warned about (hardcoded secrets in source).

PRIVATE_KEY_RE = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
TOKEN_RE = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password|passwd)\s*[=:]\s*['\"][^'\"]{12,}['\"]"
)


def detect_secrets(blob: str) -> list[str]:
    """Return human-readable descriptions of any secret-looking strings."""
    findings: list[str] = []
    if PRIVATE_KEY_RE.search(blob):
        findings.append("embedded private key block")
    for match in TOKEN_RE.finditer(blob):
        findings.append(f"suspected secret assignment: {match.group(0)[:40]}...")
    return findings


def load_from_env(name: str) -> str:
    """The right way to get a secret is from the environment, not the code.

    The research stressed never hardcoding secrets. This helper makes the
    intent obvious: the value lives outside the repo, and the code just
    reads it at runtime.
    """
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} is not set - store secrets in the environment.")
    return value


# ---------------------------------------------------------------------------
# Habit 3: safe deserialization
# ---------------------------------------------------------------------------

def parse_xml(xml_text: str) -> dict[str, str]:
    """Parse untrusted XML defensively.

    The naive path uses xml.etree.ElementTree.fromstring, which the research
    flags as enabling XXE and billion-laughs. The hardened path prefers a
    parser that refuses entity expansion. I use defusedxml when it is
    available, and otherwise do an explicit guard that rejects the DTD
    entities used by those attacks.
    """
    try:
        from defusedxml import ElementTree as SafeET
    except ImportError:
        SafeET = None

    if SafeET is not None:
        root = SafeET.fromstring(xml_text)
        return {child.tag: (child.text or "") for child in root}

    lowercase = xml_text.lower()
    if "<!doctype" in lowercase or "<!entity" in lowercase:
        raise ValueError("refusing to parse XML with a DTD/entity (XXE / billion-laughs risk)")
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_text)
    return {child.tag: (child.text or "") for child in root}


# ---------------------------------------------------------------------------
# demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Habit 2: show the detection working.
    sample = 'password = "super-insecure-123456"; api_key = "ak_live_9f8"'
    leaks = detect_secrets(sample)
    print(f"Secrets detected in sample: {leaks}")

    key = load_from_env("EXAMPLE_API_KEY")
    print(f"Loaded EXAMPLE_API_KEY safely: {'set' if key else 'empty'}")

    # Habit 3: safe parsing.
    good = "<config><user>alice</user><role>viewer</role></config>"
    print(f"Parsed good XML: {parse_xml(good)}")
    try:
        evil = '<?xml version="1.0"?><!DOCTYPE x [<!ENTITY a "boom">]><r>&a;</r>'
        print(f"Parsed entity XML: {parse_xml(evil)}")
    except ValueError as exc:
        print(f"Blocked entity XML: {exc}")

    # Habit 1: run only when invoked explicitly; pass --scan to actually
    # shell out to pip-audit so plain runs stay side-effect-free.
    if "--scan" in sys.argv:
        scan_dependencies()
