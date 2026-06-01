# tox — quick primer

> First-day notes for someone who's never used tox. Personal voice, plain language.

## What is it?

I just installed tox. It runs tests in isolated virtualenvs so I don't fight "works on my machine" bugs. Instead of running `pytest` globally, it creates a fresh env per config section, installs only the deps I list, and runs commands from scratch. Think of it as a CI runner stored in a config file — same harness locally and remotely.

## What does it do?

I write a `tox.ini`, list envs like `py311`, add deps and commands. Running `tox` builds `.tox/`, installs into fresh envs, and runs each command. Each env is independent — one failure doesn't block the others.

## Why does it exist?

Before tox, teams wrote ad-hoc shell scripts or relied only on CI. I'd hit version conflicts running `pytest` globally, or wait for CI to catch a "only on 3.10" bug. tox makes the same test harness available on my laptop.

## Key terminology

- **envlist** — envs that run by default, e.g. `py311`
- **deps** — packages tox installs before commands
- **commands** — shell commands tox runs in order
- **tox.ini** — the config file defining envs, deps, and commands

## A tiny example

```ini
[tox]
envlist = py311

[testenv]
deps = pytest
commands = pytest
```

I put this in a project with one test file and ran `tox`. Fresh venv, install, run, pass.

## What I'll cover next

Multiple envs side by side and a lint env with ruff.
