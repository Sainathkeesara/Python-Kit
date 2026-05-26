# pre-commit — quick primer

> First-day notes for someone who's never used pre-commit. Personal voice, plain language.

## What is it?

pre-commit is a framework for managing and running "git hooks" — those scripts that fire before a commit, push, or other git event. Think of it like a CI pipeline that runs on your laptop before code ever reaches GitHub. It's to git hooks what a package manager is to libraries: instead of hand-writing shell scripts in `.git/hooks/` and hoping they work on every teammate's machine, you declare what checks you want in a YAML file and pre-commit handles the rest.

I've heard it compared to Ruff's `--fix` or a linter, but it's more general — it can run *anything* as long as it's a command that exits 0 on success.

## What does it do?

You write a `.pre-commit-config.yaml` listing hooks (like "trim trailing whitespace", "check for merge conflicts", "run Ruff", "run mypy"). pre-commit installs itself into your git hooks directory, and every time you `git commit`, it stages your changed files, runs each hook against them, and either passes (lets the commit through) or fails (blocks the commit). Some hooks can even fix the files automatically.

## Why does it exist?

Before pre-commit, teams had to either (a) manually remind each other to lint before committing, (b) trust CI to catch everything after pushing, or (c) write and maintain fragile shell scripts in `.git/hooks/` that didn't get version-controlled easily. pre-commit makes hooks reproducible across a team and version-controlled alongside the code. Every dev gets the same set of checks running at the same point in the workflow.

## Key terminology

- **Hook** — A single check or task that runs on your code. Example: `check-yaml` validates that `.yaml` files parse correctly.
- **Repo** — A source of hooks. Most hooks come from the `pre-commit-hooks` repo on GitHub (the "meta" repo maintained by the pre-commit team), but you can use any repo that publishes `.pre-commit-hooks.yaml`.
- **ID** — The name of a hook inside a repo. In `.pre-commit-config.yaml`, you tell it which `repo:` and which hook `id:` to use.
- **Stage** — Which git event triggers the hook (`pre-commit` is default, but you can set `pre-push`, `commit-msg`, etc.).
- **`rev`** — The tagged version of the hook repo to pin. Without this, different team members could run different hook versions.
- **Skip** — Setting `SKIP=hook-id git commit` bypasses a specific hook for one commit. Useful when you know the lint failure is intentional.
- **`files` / `exclude`** — Patterns to narrow which files a hook runs on.

## A tiny example

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: check-json
      - id: check-yaml
```

Then run `pre-commit install` and the hooks fire on every `git commit`.

## What I'll cover next

I want to add Ruff and mypy as pre-commit hooks, try auto-fixing on commit, and figure out how to run hooks selectively on only staged files (the default seems to already do this, but I want to confirm).
