---
last_verified: 2026-08-11
tool_version: n/a
sources:
  - https://docs.astral.sh/uv/guides/integration/github/
  - https://pydevtools.com/handbook/how-to/how-to-manage-cross-repo-python-dependencies-with-uv/
  - https://www.danilchenko.dev/posts/uv-workspaces-monorepo/
---

# Git workflows for the Python learning kit

## Purpose

This doc ties together the Git workflow the Python-Kit uses day to day: a branch-and-PR flow, semantic tags for releases, and CI gates that check every push. The point is one reproducible pipeline — branches for isolation, tags as the release point, and CI as the gate that keeps unverified code from merging.

## When to use

- Any change that touches more than a one-line fix gets its own branch and pull request.
- Releasing a tool note or a versioned library needs a tag.
- CI gates run on every push and every pull request — before merge, never after.

## Prerequisites

- A Git repository with `main` as the default branch.
- `[tool.uv.sources]` and `uv.lock` committed, so dependency resolution is reproducible for every checkout (this is what makes CI results match local runs). The `.gitignore` keeps `.venv/`, `dist/`, and `__pycache__/` out of history so the repo stays clean.
- A CI runner (GitHub Actions in this kit) with uv available.

## Steps

1. **Branch for the work.** Create a feature branch off `main` (`git checkout -b add-tool-note`), commit in small logical units, and push.
2. **Open a pull request.** The PR is where review and the CI gates happen. Branch protection requires the pytest status check to pass before merge.
3. **Tag the release.** When the branch merges and the change is ready to ship, tag it with a version like `v1.2.0`. Tags are the fixed point that dependents pin against — `uv add "shared-lib @ git+https://github.com/acme/shared-lib" --tag v1.2.0` pins the source inside `[tool.uv.sources]` to that tag.
4. **Let the lockfile pin the code.** A branch pin drifts by design; a tag or rev pin is fixed. The lockfile records the resolved commit SHA, so every `uv sync` pulls the same code until `uv lock --upgrade-package shared-lib`.
5. **CI caches uv.** On GitHub Actions, `astral-sh/setup-uv` with `enable-cache` caches the uv install, and `uv cache prune --ci` trims cache size after the tests run.

## Verify

- `git status` shows a clean tree on `main` after a merge.
- The release tag exists locally and on the remote (`git tag` lists `v1.2.0`).
- CI on the PR branch is green before merge; the merged commit on `main` is the same code that was tested.

## Common errors

- **Branch pin drift.** Using `--branch main` instead of `--tag v1.2.0` means the dependency moves whenever the branch moves. Reach for `--tag`/`--rev` when a fixed point is wanted.
- **Workspace isolation gap.** In a monorepo all members share one `.venv`, so any package can import anything installed for another member. Run ruff with an import-boundary check in CI so an undeclared import fails the build instead of shipping.

## References

- https://docs.astral.sh/uv/guides/integration/github/
- https://pydevtools.com/handbook/how-to/how-to-manage-cross-repo-python-dependencies-with-uv/
- https://www.danilchenko.dev/posts/uv-workspaces-monorepo/
