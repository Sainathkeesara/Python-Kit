# Explored pyproject.toml's build-system config

I made a minimal pyproject.toml with just the `[build-system]` table to see what it actually controls. I'd been cargo-culting this section for a while.

## What I put in

```toml
[build-system]
requires = ["setuptools>=64", "wheel"]
build-backend = "setuptools.build_meta"
```

That's it. `requires` tells pip/uv which packages to install before running the build. `build-backend` is the actual builder function — setuptools reads `setup.cfg` or `setup.py` for the rest.

## What I learned

- Without `[build-system]`, pip/uv fall back to legacy setuptools behavior (which works but shows a deprecation warning). With it, the build is fully PEP 517/621 compliant.
- `requires` can list anything — `hatchling`, `flit_core`, `pdm-backend` — as long as `build-backend` matches.
- The `[project]` table (name, version, deps) is separate from `[build-system]`. The build-system is just about *how* to build; `[project]` is *what* you're building.
- Both are needed for a publishable package, but `[build-system]` alone + a `setup.cfg` is enough for a local editable install.

Next I want to add `[project]` with a real name and some dependencies, then try `pip install -e .` to see it all connect.
