# Repository Structure

This document describes the directory layout of Python-Kit.

## Top-level directories

| Directory | Purpose |
|-----------|---------|
| `00_index/` | Navigation files including quick-links.md, topics.md, glossary.md |
| `uv/` | Notes, scripts, configs, and snippets for Astral's uv package manager |
| `py/` | Ruff and related Python tooling notes, scripts, configs |
| `py-spy/` | Profiler notes and scripts for py-spy |
| `pytest/` | pytest testing framework notes and snippets |
| `pyproject.toml/` | pyproject.toml configuration notes and examples |
| `uv.lock/` | uv.lock lock file notes and scripts |
| `pre-commit/` | pre-commit hook configuration and scripts (scripts/, notes/, snippets/) |
| `pip-audit/` | Vulnerability scanning notes and scripts |
| `pipdeptree/` | Dependency tree notes and scripts |
| `mypy/` | Type checking notes and test scripts |
| `rich/` | Terminal output notes, scripts, and snippets |
| `ty/` | Type checker comparison notes and configs |
| `ruff/` | Linter/formatter notes, configs, and comparisons |
| `typer/` | CLI framework notes and demos |
| `httpie/` | API testing CLI notes, scripts, and configs |
| `tox/` | Test automation notes and configs for tox |
| `docs/` | Project-level documentation (repository-structure.md) |

## File organization by type

| Type | Directory | Extension |
|------|-----------|-----------|
| Notes (primer) | `<tool>/notes/0000-primer-<tool>.md` | `.md` |
| Notes (dated) | `<tool>/notes/<YYYY-MM-DD>-<topic>.md` | `.md` |
| Snippets | `<tool>/snippets/<topic>.<ext>` | `.py`, `.sh`, etc. |
| Scripts | `<tool>/scripts/<topic>.<ext>` | `.sh`, `.py` |
| Configs | `<tool>/configs/<topic>.<fmt>` | `.toml`, `.yaml` |
| Manifests | `<tool>/manifests/<topic>.<fmt>` | `.yaml` |

## Quick reference

- `README.md` — Project overview
- `CHANGELOG.md` — Recent changes log
- `uv.lock` — Lock file for uv dependencies (if present)
