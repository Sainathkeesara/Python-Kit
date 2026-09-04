# dep-hygiene — dependency hygiene scaffold

A src-layout Python package with pipdeptree + pip-audit wired up for
continuous dependency health checks.

## What this scaffold includes

- **src-layout package** (`src/dep_hygiene/`) — keeps installed code separate
  from repo source.
- **pipdeptree** tool table in `pyproject.toml` — excludes virtualenv and
  build artefacts from the dependency tree output.
- **pip-audit** tool table in `pyproject.toml` — ignores dev-only
  directories; the audit script exports a lockfile and scans it without
  rebuilding a venv.
- **scripts/** — two helper scripts for running the dependency health checks.

## Prerequisites

- Python 3.11+
- uv (https://docs.astral.sh/uv/)

## Setup

```bash
uv sync --all-extras
```

## Run the dependency health check

```bash
uv run python scripts/audit_deps.py
```

This prints a JSON report covering the dependency tree, version conflicts,
cyclic dependencies, and reverse-dependency hotspots. Exits non-zero if
cycles are found.

## Run pip-audit

```bash
bash scripts/audit_deps.sh
```

Exports the resolved lockfile via `uv export`, then runs `pip-audit` against
it. Exits non-zero if any vulnerability is found.

## Why both tools

pipdeptree and pip-audit cover different parts of dependency hygiene:
pipdeptree surfaces structural problems (conflicts, cycles, unexpected
transitive deps) while pip-audit queries vulnerability databases against
the resolved dependency set. Running both on every PR catches a broader
range of issues than either alone.
