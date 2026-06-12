# Figured out which Python quality tools belong together

I've been installing these tools one at a time — Ruff for linting, mypy for types, pytest for tests, pre-commit to run them automatically, uv to install everything. It took me a while to realize they're meant to work as a chain, not standalone.

Here's what I settled on for a fresh project:

1. **uv** creates the environment and installs everything
2. **Ruff** lints and formats — this is the fastest gate, run it first
3. **mypy** checks types — slower but catches a different class of bugs
4. **pytest** runs tests — last because tests assume the code is at least valid

I wired these into a simple script that runs them all in order (gen-004 does this). If Ruff fails I stop — no point type-checking broken code.

Pre-commit sits on top of this chain. Every commit runs Ruff + mypy on the staged files only. Same pipeline, but faster since it's incremental.

One thing that tripped me up: I kept running mypy with `--strict` on code that Ruff hadn't even linted yet. The error messages overlap — Ruff catches `F821` (undefined name) which mypy also flags. Running Ruff first means mypy gets cleaner input and its output is more useful.

Next I want to add `tox` to this chain so the whole thing runs against Python 3.10, 3.11, 3.12 in CI.
