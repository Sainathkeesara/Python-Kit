# Reading uv.lock — what I found inside

I generated a `uv.lock` by running `uv add requests` in a fresh project, then opened it to see what's in there. Here's what I found:

## Top-level layout

The file is TOML. First thing I see is a `[metadata]` section with a `manifest-hash` — a SHA256 of `pyproject.toml` so uv knows if I changed deps. Then a big list of `[[package]]` entries.

## A `[[package]]` entry

Each one has `name`, `version`, `source`, and `dependencies`. For example:

```toml
[[package]]
name = "requests"
version = "2.32.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
```

Transitive deps like `certifi` and `urllib3` each get their own `[[package]]` entry too. uv resolved the whole tree.

## What surprised me

- The file is sorted alphabetically by package name, not by dependency depth.
- Each wheel has a `sdist` and `wheels` list with hashes — uv verifies integrity when installing.
- There's no `requires-python` per-package; that lives in `[metadata]` at the top.

## What I'd do differently next time

I want to compare a lockfile from `uv add flask` vs `uv add django` to see how different dep trees look.
