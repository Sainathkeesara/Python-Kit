---
last_verified: 2026-08-09
tool_version: n/a
sources: []
---

# Set up my first pre-commit hook and ran it once

I installed pre-commit for the first time today and walked through the full setup: install, config, first run. This is my scratch notes on what happened.

## Installing

`pip install pre-commit` got it installed. Then `pre-commit --help` showed me the subcommands. The one I needed was `install`, which writes a shim into `.git/hooks/pre-commit`. I ran it from the repo root and it worked.

## The config

I ran `pre-commit sample-config > .pre-commit-config.yaml` to get a starter file. Then I added ruff to it:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.20
    hooks:
      - id: ruff
        args: [--fix]
        types: [python]
```

I pinned the rev to a specific tag — the docs recommend never using `main` or `HEAD` because upstream can break without warning.

## First run

I created a test file with a bad import order and trailing whitespace. Committed it with `git add . && git commit`. The pre-commit hook fired and ruff fixed both issues automatically. The commit went through clean.

## What caught me

`pre-commit run --all-files` is what I needed to lint the whole repo at once — the hook only runs on staged files by default, so existing files don't get checked unless I use `--all-files`.

To skip a hook for one commit: `SKIP=ruff git commit -m "wip: rough draft"` — that's cleaner than `--no-verify` which skips everything.

## What I'd try next

Add `check-yaml` and `end-of-file-fixer` from `pre-commit-hooks` rev `v6.0.0`, then try `pre-commit run --all-files --show-diff-on-failure` to see what the diff looks like.
