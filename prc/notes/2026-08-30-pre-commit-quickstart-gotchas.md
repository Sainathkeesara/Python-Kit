---
last_verified: 2026-08-30
tool_version: n/a
---

# Following the pre-commit quickstart — what tripped me up

I went through the pre-commit quickstart last week and got most of it working, but three things kept biting me: local hooks, the `--hook-stage` flag, and how arguments get passed to hooks. Here's what I learned the hard way.

## What the quickstart covers

The quickstart walks you through installing pre-commit, generating a `.pre-commit-config.yaml` with `pre-commit sample-config`, and running `pre-commit install` to wire the hook into `.git/hooks/pre-commit`. That part was smooth. I got ruff and trailing-whitespace hooks running on `git commit` within a few minutes.

## Got stuck on: local hooks

I wanted to add a custom script that lives in my repo, not one from an external repo. The quickstart points mostly at remote repos like the pre-commit-hooks collection, so I had to figure out the `repo: local` syntax myself.

The key insight: with `repo: local`, you skip the `rev` field entirely and define hooks inline under `hooks:`. I kept trying to add a `rev` because every example in the quickstart used one. Once I dropped it, the local hook started showing up in `pre-commit run --all-files`.

## Got stuck on: --hook-stage

`pre-commit run` by itself only runs `pre-commit` stage hooks — the ones that fire before a commit. I wrote a `commit-msg` hook and ran `pre-commit run` expecting it to fire. It didn't.

The fix is `pre-commit run --hook-stage commit-msg`. The stages map directly to git's hook names: `pre-commit`, `pre-push`, `commit-msg`, `pre-rebase`, etc. If you're not sure what stage a hook is registered for, `pre-commit run --all-stages` runs everything so you can see what's available.

## Got stuck on: pass_args

I had a hook that needed a flag passed to it, like `mypy --strict`. I kept editing the hook's entry script to hardcode the flag. That works, but it means every invocation is stuck with `--strict` even when I don't want it.

The right approach is the `args` key in `.pre-commit-config.yaml`:

```yaml
- id: mypy
  args: ["--strict"]
  pass_filenames: false
```

`args` appends arguments to whatever the hook normally runs. I also learned that `pass_filenames: false` matters here — if filenames get passed automatically and my tool doesn't expect them, it errors out. For `mypy`, the default `pass_filenames: true` is fine because it takes files. For something like `black` that I want to run on the whole codebase, I flip it to `false` and pass explicit paths via `args` or rely on black's own file discovery.

## What I'd try next

I want to wire a `pre-push` hook that runs a quick smoke test before anything goes remote. The `--hook-stage` flag should make that straightforward. I also want to try `pre-commit try-repo` to test an updated hook version without changing my pinned config.
