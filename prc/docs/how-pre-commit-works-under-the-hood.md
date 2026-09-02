---
last_verified: 2026-09-02
tool_version: 4.6.2
sources:
  - https://pre-commit.com/
  - https://pre-commit.com/#supported-git-hooks
  - https://pre-commit.com/#confining-hooks-to-run-at-certain-stages
  - https://pre-commit.com/#passing-arguments-to-hooks
---

# How pre-commit works under the hood

This doc explains what pre-commit actually does when it runs your hooks — the stage system, how filenames flow into hooks, environment variables you can pass, and the debugging toolkit when something breaks.

## Hook stages: what triggers what

pre-commit supports ten git hook types, not just `pre-commit`. Each maps to a specific point in the git workflow:

| Stage | Git event | When it fires |
|-------|-----------|---------------|
| `pre-commit` | `git commit` | Before the commit object is created; hooks can block or modify files |
| `pre-merge-commit` | merge succeeds (git ≥2.24) | After merge resolution, before the merge commit is created |
| `pre-push` | `git push` | After local commits pass but before they reach the remote |
| `commit-msg` | `git commit` | Receives the commit message file; can rewrite or reject it |
| `prepare-commit-msg` | `git commit` | Before the editor opens; can modify the draft message |
| `pre-rebase` | `git rebase` | Before a rebase starts; failure cancels the rebase |
| `post-checkout` | `git checkout` | After a checkout completes; useful for setup or cleanup |
| `post-commit` | `git commit` | After the commit succeeded; cannot block anything |
| `post-merge` | `git merge` | After a successful merge |
| `post-rewrite` | `git commit --amend` / `git rebase` | After history-modifying commands |

By default, hooks run on **all** stages unless you confine them. You restrict which stage a hook runs on via the `stages` property:

```yaml
repos:
  - repo: https://github.com/PyCQA/mypy
    rev: v1.14.1
    hooks:
      - id: mypy
        stages: [pre-push]  # only fire on push, not on every commit
```

Since pre-commit 3.2.0, stage values match the hook names directly (e.g. `pre-push`, not `push`). The special `manual` stage never triggers automatically — run it explicitly with `pre-commit run --hook-stage manual <hook-id>`.

To install hooks for multiple stages, pass `--hook-type` multiple times:

```bash
pre-commit install --hook-type pre-commit --hook-type pre-push
```

Or set `default_install_hook_types` at the top of your config:

```yaml
default_install_hook_types: [pre-commit, pre-push, commit-msg]
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: commit-msg-linter
```

## pass_filenames: how staged files reach your hook

When `pass_filenames` is `true` (the default), pre-commit passes the staged filenames as arguments to the hook entry point. The hook receives:

```
<entry> <args> <file1> <file2> <file3>
```

For example, with this config:

```yaml
- id: ruff
  args: [--fix]
  pass_filenames: true
  types: [python]
```

pre-commit calls something like:

```
ruff --fix src/main.py src/utils.py tests/test_main.py
```

Key behaviors:

- **Only staged files are passed.** pre-commit stashes unstaged changes, runs hooks on the staged snapshot, then restores. This prevents false positives from uncommitted work.
- **Batching.** When many files are staged, pre-commit splits them into batches (default: 400 files per batch) to avoid exceeding OS argument-length limits.
- **`types` filters first.** The `types` and `files` properties narrow which staged files reach the hook. A hook with `types: [python]` never sees `.yaml` files even if they are staged.

When `pass_filenames` is `false`, the hook receives only `args` — no filenames. Use this for tools that discover files internally:

```yaml
- id: pytest
  pass_filenames: false
  entry: pytest tests/ -q
  types: [python]
```

Setting `pass_filenames` to a positive integer limits the batch size. For example, `pass_filenames: 1` calls the hook once per file instead of batching:

```yaml
- id: my-slow-checker
  pass_filenames: 1  # one file at a time
```

## Environment variables: pass_env and stage-specific vars

pre-commit injects several environment variables during hook execution:

**Always available:**
- `PRE_COMMIT=1` — lets your hook detect it is running inside pre-commit (set since v2.5.0).

**Stage-specific variables** (set on the corresponding git hook type):

| Variable | Stage | What it contains |
|----------|-------|-----------------|
| `PRE_COMMIT_FROM_REF` | `post-checkout`, `pre-push` | The source ref (e.g. branch being pushed) |
| `PRE_COMMIT_TO_REF` | `post-checkout`, `pre-push` | The destination ref |
| `PRE_COMMIT_CHECKOUT_TYPE` | `post-checkout` | `1` for branch checkout, `0` for file checkout |
| `PRE_COMMIT_REMOTE_NAME` | `pre-push` | The remote name (e.g. `origin`) |
| `PRE_COMMIT_REMOTE_URL` | `pre-push` | The remote URL |
| `PRE_COMMIT_REMOTE_BRANCH` | `pre-push` | Target remote branch (e.g. `refs/heads/main`) |
| `PRE_COMMIT_LOCAL_BRANCH` | `pre-push` | Local branch being pushed |
| `PRE_COMMIT_IS_SQUASH_MERGE` | `post-merge` | Whether the merge was a squash merge |
| `PRE_COMMIT_REWRITE_COMMAND` | `post-rewrite` | The command that triggered the rewrite |
| `PRE_COMMIT_COMMIT_MSG_SOURCE` | `prepare-commit-msg` | How the message was generated |
| `PRE_COMMIT_COMMIT_OBJECT_NAME` | `prepare-commit-msg` | The commit object SHA |

To **pass custom environment variables** to a hook, use the `env` property (in `.pre-commit-hooks.yaml` for hook authors, or via `additional_dependencies` in the consumer config):

```yaml
- id: my-custom-hook
  entry: my-script
  language: python
  env:
    MY_API_KEY: "test-only"
    LOG_LEVEL: debug
```

Hooks running with `language: unsupported` (formerly `system`) do not get an isolated environment — they inherit the full shell environment. This is useful for tools that need system-level packages.

## Debugging a failing hook

When a hook fails during `git commit`, pre-commit shows the hook name, exit code, and output. But sometimes that is not enough. Here is the debugging toolkit:

### 1. Verbose output

```bash
pre-commit run --verbose --all-files
```

This prints the exact command pre-commit runs for each hook, plus the hook's stdout regardless of pass/fail.

### 2. Show the diff on failure

```bash
pre-commit run --show-diff-on-failure
```

When a hook modifies files (like `ruff --fix`), this runs `git diff` immediately after so you can see exactly what changed. Essential for debugging auto-fixers.

### 3. Run a single hook

```bash
pre-commit run ruff --all-files
```

Isolate the problem to one hook instead of running the full suite.

### 4. Run against specific files

```bash
pre-commit run --files src/main.py src/utils.py
```

Bypass the staged-files detection to test on the exact files you suspect.

### 5. Run against a commit range

```bash
pre-commit run --from-ref HEAD~3 --to-ref HEAD
```

Catches what the last three commits introduced. Useful for CI or post-merge checks.

### 6. Skip a specific hook

```bash
SKIP=ruff git commit -m "skip lint for now"
```

The `SKIP` variable is a comma-separated list of hook IDs. This is better than `--no-verify` because it only bypasses the named hook — other hooks still run.

### 7. Clean cached environments

```bash
pre-commit clean
```

When a hook's environment is corrupted (missing system deps, stale node/npm install, wrong Python version), cleaning the cache forces a fresh install on the next run.

### 8. Try a local hook repo

```bash
pre-commit try-repo ../my-hook-repo my-hook-id --verbose --all-files
```

Useful when developing your own hook — test it without committing to the config.

### Common failure patterns

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `hook id: X` + exit code 1, no further output | Hook ran but produced no output on stdout/stderr | Run with `--verbose` to see the full command |
| `pre-commit not found` | `pre-commit install` was never run | Run `pre-commit install` from the repo root |
| Hook passes locally but fails in CI | Missing system dependency or different environment | Check the hook's language; use `additional_dependencies` or `language: unsupported` |
| Files modified by hook, commit fails | Auto-fixer ran but changes are unstaged | `git add` the modified files and recommit |
| `language X is not supported` | pre-commit version too old | `pip install --upgrade pre-commit` |
| Stale hook environment | Hook repo updated but cache is old | `pre-commit clean && pre-commit autoupdate` |

## Verify

Run this to confirm your hooks are wired correctly:

```bash
pre-commit run --all-files --verbose
```

Every hook should show its full command, the files it processes, and either `Passed` or `Failed` with actionable output. If a hook shows `(no files to check) Skipped`, the `types`/`files` filter is not matching any staged files — check your file patterns.
