---
last_verified: 2026-08-24
tool_version: n/a
sources: []
---

# Security Best Practices — quick primer

> First-day notes on Security Best Practices. What it is, why it matters, and the key ideas to know.

## What is it?

Security best practices are the habits and patterns that keep your code, dependencies, and deployments from being exploited. I think of it like locking your front door — not because I expect a break-in tonight, but because the cost of *not* locking is way higher than the effort of locking.

In Python, this mostly means: don't trust user input, keep your dependencies patched, don't hardcode secrets, and run tools that catch common mistakes before you ship. It's less about a single library and more about a set of practices woven into how you write and deploy code.

## Why does it matter for Python?

Python is everywhere — web backends, data pipelines, CLI tools, automation scripts. That ubiquity makes it a target. A leaked API key in a public repo, an unvalidated input in a Flask route, or a pinned-but-vulnerable dependency can all lead to real incidents. The good news is that the Python ecosystem has solid tooling to catch most of these issues early.

## Key terminology

- **Dependency scanning** — checking your installed packages against known vulnerabilities. Example: running `pip-audit` to find CVEs in your `requirements.txt`.
- **Secrets management** — keeping API keys, passwords, and tokens out of source code. Example: using environment variables or a vault instead of committing `.env` files.
- **Input validation** — verifying that data from users/files/network matches expected types and ranges before processing it. Example: rejecting a negative quantity in an order form.
- **Least privilege** — giving code only the permissions it needs. Example: a read-only database user for a reporting script instead of the admin account.
- **Static analysis** — tools that scan code without running it to find security anti-patterns. Example: `bandit` catching `eval()` calls or `assert` statements in shipped code.
- **SBOM (Software Bill of Materials)** — a machine-readable list of every component in your project, useful for tracking which vulnerabilities affect you.

## A concrete example

Here's a quick before-and-after showing how a simple security practice (input validation + secrets hygiene) changes real code:

```python
# BEFORE — vulnerable
import os
API_KEY = "sk-live-abc123"  # hardcoded secret

def process(data):
    return eval(data)  # arbitrary code execution


# AFTER — safer
import os
import re

API_KEY = os.environ["API_KEY"]  # secret from env

def process(data: str) -> int:
    if not re.fullmatch(r"\d+", data):
        raise ValueError("input must be digits only")
    return int(data)
```

The second version pulls the key from the environment and validates input before using it. Neither change is complicated, but together they close two common attack vectors.

## How this connects to what's next

Once I internalize these basics, the next step is automating them: tools like `bandit` for static analysis, `pip-audit` for dependency scanning, and pre-commit hooks to enforce secrets checks on every commit. The practices are simple; the value comes from making them automatic so they happen even when I forget.
