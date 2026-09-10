---
last_verified: 2026-09-09
tool_version: n/a
sources:
  - https://pre-commit.com/#hooks
  - https://pre-commit.com/#developing-hooks-locally
---

# Writing a custom pre-commit hook

Purpose: walk through creating a Python-based pre-commit hook from scratch — the script itself, the `.pre-commit-hooks.yaml` entry point, and how `pass_filenames` delivers staged file paths to the script.

## When to use

Custom hooks fill the gap when no existing repo covers your check. Typical cases: enforcing internal naming conventions, validating generated files (protobuf stubs, OpenAPI specs), running a project-specific linter that wraps an existing tool with extra logic, or gating on metadata that generic linters ignore.

## Prerequisites

- A Python script that does the check (can be any Python >= 3.9).
- A git repo with `pre-commit` installed and `pre-commit install` run.
- Familiarity with the `pre-commit` YAML config format (the quick-start notes cover this).

## Steps

### 1. Write the checker script

The hook script receives filenames as positional arguments when `pass_filenames: true` (the default). Exit 0 for pass, non-zero for fail.

```python
#!/usr/bin/env python3
"""Check that every Python file has a module-level docstring."""

import sys

def check_file(path: str) -> bool:
    with open(path) as f:
        lines = f.readlines()
    # skip shebangs and encoding declarations
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith(("#!", "# -*-", "# coding")):
            return stripped.startswith('"""') or stripped.startswith("'''")
    return False  # empty file — treat as fail

def main() -> int:
    failed = []
    for path in sys.argv[1:]:
        if path.endswith(".py") and not check_file(path):
            failed.append(path)
    if failed:
        print("Files missing module docstring:")
        for f in failed:
            print(f"  {f}")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Key points:

- The script must be executable (`chmod +x`).
- It reads filenames from `sys.argv[1:]` — pre-commit appends them after any `args` you define.
- Exit code 0 = pass, anything else = fail. pre-commit prints stdout/stderr on failure.

### 2. Declare the hook in `.pre-commit-hooks.yaml`

Place this file in the **root of the hook repository** (not the consuming repo). This is what consumers reference:

```yaml
- id: check-module-docstring
  name: Check module docstring
  entry: check_module_docstring.py
  language: python
  types: [python]
  pass_filenames: true
```

| Field | Purpose |
|-------|---------|
| `id` | Unique identifier — consumers reference this in their `.pre-commit-config.yaml`. |
| `name` | Human-readable label shown in pre-commit output. |
| `entry` | The script to run. Can be a script name (if on `PATH` within the env) or a path relative to the repo root. |
| `language` | `python` creates an isolated venv and installs `additional_dependencies` if any. |
| `types` | File-type filter — only files matching these types are passed. |
| `pass_filenames` | `true` (default) passes staged filenames as positional args. |

### 3. Consume the hook from another repo

In the consuming project's `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/yourorg/pre-commit-hooks
    rev: v0.1.0
    hooks:
      - id: check-module-docstring
```

Or use `repo: local` for hooks that live inside the same repo:

```yaml
repos:
  - repo: local
    hooks:
      - id: check-module-docstring
        name: Check module docstring
        entry: scripts/check_module_docstring.py
        language: system
        types: [python]
```

`language: system` means pre-commit does not create an isolated venv — it runs the script with whatever Python is on the caller's `PATH`.

### 4. Test before publishing

```bash
pre-commit try-repo ../my-hook-repo check-module-docstring --verbose --all-files
```

This runs the hook against every file in the current repo without modifying `.pre-commit-config.yaml`. Useful during development.

## Verify

After wiring everything:

```bash
pre-commit run check-module-docstring --all-files
```

The output should show either `Passed` or `Failed` with the list of files missing docstrings. A `Skipped` result means the `types` filter is not matching any staged files — check that your staged files are `.py`.

## Common errors

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `hook id: check-module-docstring` + exit 1, no output | Script printed to stderr, which pre-commit suppresses on pass | Use `print()` (stdout) for messages; stderr only appears on failure |
| `Not Found` when consuming the hook | `repo:` URL or `rev:` tag does not match the hook repo | Verify the repo URL is reachable and the tag/branch exists |
| Script runs but receives no filenames | `pass_filenames: false` or `types` filter excludes your files | Check `.pre-commit-hooks.yaml` — ensure `pass_filenames: true` and `types` matches |
| `language: python` hook fails with missing deps | `additional_dependencies` not listed | Add required packages under `additional_dependencies` in the hook declaration |
| Hook works locally but fails in CI | CI uses a different Python version or missing system deps | Pin Python version in CI; use `language: system` if the tool is pre-installed |
