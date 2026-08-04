---
last_verified: 2026-08-04
tool_version: n/a
---

# uv.lock — how the lockfile maps to pyproject.toml dependencies

> What I learned opening uv.lock and tracing each entry back to pyproject.toml.

## What I did

I ran `uv lock` on a small project and then opened the generated `uv.lock` file alongside `pyproject.toml` to see how the two files relate. I was surprised by how much detail the lockfile carries beyond what pyproject.toml declares.

## Steps

1. Created a minimal project with `uv init` and added `requests` and `httpx` as dependencies in `pyproject.toml`.
2. Ran `uv lock` to generate `uv.lock`.
3. Opened `uv.lock` and compared the `[[package]]` entries against the `[project.dependencies]` section in `pyproject.toml`.
4. Traced how each direct dependency in pyproject.toml appears in uv.lock with its exact pinned version, and how transitive dependencies (packages that those direct deps depend on) also appear.

## What I noticed

In `pyproject.toml`, I listed `requests` with a version range like `>=2.28`. In `uv.lock`, that same package appears with an exact version (`2.31.0`) and a hash. The lockfile also lists every transitive dependency — packages that `requests` itself depends on — each with their own exact version and hash. So pyproject.toml declares *what you want*, and uv.lock records *exactly what you get*.

The `[[package]]` entries in uv.lock include `name`, `version`, `source`, and `dependencies` fields. The `source` field tells you whether the package came from PyPI, a git repository, or a local path. That's useful for debugging when a dependency isn't where you expect it.

## What tripped me up

I kept expecting uv.lock to be a simple flat list, but it's actually a TOML document with nested arrays of tables. The `[[package]]` syntax means each package is its own table, and the `dependencies` field inside each package is an array of strings listing that package's own deps. It took me a few reads to see the tree structure.

I also confused the `uv lock` command (which generates the lockfile) with `uv sync` (which reads the lockfile and installs). They do different things — `uv lock` resolves and writes, `uv sync` installs from what's already written.

## What I'd try next

I want to see what happens when I edit pyproject.toml to change a version constraint and re-run `uv lock` — does the lockfile update only the affected packages or does it re-resolve everything? I'd also like to try `uv lock --no-dev` to see how dev dependencies are excluded from the lockfile.