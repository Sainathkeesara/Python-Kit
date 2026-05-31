# tox — quick primer

> First-day notes for someone who's never used tox. Personal voice, plain language.

## What is it?

tox is a test automation tool that manages virtual environments for testing. If you've run `pytest` locally only to find it fails due to missing deps, tox solves that — it creates isolated envs automatically and installs exactly what you list. Think of it as "CI but on your laptop."

## What does it do?

It reads `tox.ini`, spins up virtual environments per your config, installs deps, and runs commands (usually tests). You define environments like `py311` or `lint`, and `tox` runs them all. Each env is isolated — no pollution between runs.

## Why does it exist?

Before tox, testing multiple Python versions meant ad-hoc scripts or waiting for CI. If tests only fail on Python 3.10 but you're on 3.11, you'd never know until the CI runs. tox brings that matrix testing to your machine.

## Key terminology

- **Environment** — A tox-managed virtualenv (e.g., `py311`).
- **deps** — Packages installed in each env.
- **commands** — What tox runs inside each env.
- **tox.ini** — The config file defining envs.
- **envlist** — Which envs run by default.

## A tiny example

```ini
[tox]
envlist = py311

[testenv]
deps = pytest
commands = pytest
```

Run `tox` — it creates `.tox/py311/`, installs pytest, runs tests.

## What I'll cover next

I want to run multiple envs side-by-side and add a lint env with ruff.