---
last_verified: 2026-08-23
tool_version: n/a
sources:
  - https://docs.astral.sh/uv/concepts/projects/layout/
  - https://docs.astral.sh/uv/guides/projects/
---

# Reading uv.lock: entries, hashes, sources, and when the file changes

## Purpose

This doc explains how to read a `uv.lock` file — the structure of individual entries, where hashes and sources appear, and what triggers the lockfile to update. The goal is to make the lockfile less opaque when troubleshooting dependency issues.

## Entry structure

A `uv.lock` file is a TOML document made of `[[package]]` array-of-tables entries. Each entry represents one resolved package and carries the fields needed to reproduce that exact install.

The core fields are:

- **name** — the package name as published to the index.
- **version** — the exact version uv resolved.
- **source** — where the package was fetched from (PyPI, a git URL, a local path, or a custom index).
- **dependencies** — a list of that package's own direct dependencies, each written as `name (>=version)` or similar constraint.
- **groups** — which dependency groups the package belongs to (default, dev, etc.).
- **optional-dependencies** — extras that were selected during resolution.

Example entry:

```toml
[[package]]
name = "requests"
version = "2.31.0"
groups = ["default"]
dependencies = [
    "certifi (>=2017.4.17)",
    "charset-normalizer (>=2,<4)",
    "idna (>=2.5,<4)",
    "urllib3 (>=1.21.1,<3)",
]
```

The `[[package]]` syntax means each package is its own table. A lockfile typically contains dozens of entries — top-level dependencies alongside all their transitive dependencies.

## Hashes

Each resolved package carries a hash that uv uses to verify the downloaded artifact hasn't changed. Hashes are recorded inside the package entry and checked at install time.

uv stores these hashes so `uv sync` installs byte-identical artifacts on every machine. If a hash is missing or mismatched, the install fails rather than silently pulling a different build.

## Sources

The `source` field distinguishes where each package came from:

- **registry** — fetched from PyPI or a custom index URL.
- **git** — pulled from a Git repository.
- **path** — a local directory or file dependency.
- **workspace** — a member of a `[tool.uv.workspace]` monorepo.

When a source is a registry, the lockfile records the index URL. This matters in CI if you mirror PyPI behind a corporate proxy — the lockfile preserves the exact source so installs don't accidentally hit the public index.

## When the lockfile changes

`uv.lock` updates whenever dependency resolution changes. Common triggers:

- Adding or removing a dependency in `pyproject.toml`.
- Changing a version constraint (e.g., `requests>=2.28` to `requests>=2.31`).
- Running `uv lock` explicitly after editing the lockfile manually.
- Switching Python version constraints in `requires-python`, which can shift the compatible set of wheels.

Small edits to `pyproject.toml` don't always cause a full re-resolve. uv tries to reuse unchanged subtrees where possible. But if a version constraint shifts, expect the affected package and its dependents to get new versions and hashes.

## Verify

To confirm you're reading the lockfile correctly:

1. Open `uv.lock` and locate a direct dependency you added (one you recognize).
2. Check its `source` field matches where you expected it to come from.
3. Verify the `dependencies` list matches the package's actual runtime requirements.
4. Run `uv lock` to confirm the lockfile is up to date with `pyproject.toml`.

If `uv lock` reports changes, the lockfile had drifted and needed a fresh resolution run.

## What I'd expand next

I'd like to look at how workspace members share lockfile entries in a monorepo, and whether `uv.lock` handles platform-specific wheels differently than source distributions.
