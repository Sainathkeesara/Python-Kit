# Tried mypy quickstart on existing projects

Ran the official mypy quickstart on one of my working codebases today. The gist: run `mypy .` and see what happens. Here's what I actually did and where I got stuck.

## What I did

1. Installed mypy with `uv add --dev mypy` — quick, no issues.
2. Ran `mypy .` at the repo root. Got 147 errors on the first pass. Most were "missing type annotation" and "incompatible type" on third-party returns.
3. Created a `pyproject.toml` section to set flags instead of typing them every time. The quickstart mentions `--strict` for new projects, but on existing code that's just noise.
4. Dialed it back to `--check-untyped-defs` and `--ignore-missing-imports` to start. That cut the error count by about half.
5. Added an `exclude` list for `migrations/`, `build/`, and `venv/` directories — these aren't my code and I don't want to see their errors.

## Where I got stuck

- `mypy .` does not recurse into `site-packages` by default (good), but it does try to type-check every `.py` file under the project root. I had to explicitly exclude generated directories.
- The quickstart example uses `--strict` and assumes a greenfield project. There's no "migrating an existing project" path in the quickstart itself — I had to piece that together from the config docs.
- `ignore_missing_imports` silences errors for packages without stubs, but it also hides real issues. I ended up installing `types-requests` and `types-pytz` separately instead of blanket-ignoring.
- The first run's output is verbose. `--show-error-codes` made it easier to group and prioritize fixes.

## What I'd try next

- Run `--strict` on a single module to see how far off from strictness that module really is.
- Try `dmypy` for faster incremental runs — the cache helps but a daemon might be better.
- Look at `--warn-unused-ignores` once I clean up the existing `# type: ignore` comments — I suspect some are stale.
