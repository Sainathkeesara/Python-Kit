# 2026-06-08-tox-quickstart.md

I followed the official tox quickstart to set up a multi-env project. I cloned a small sample repo and ran `tox` from the root. First thing it did: printed a message that tox was running in processes (no recreate) and then tried to lint and test. The `flake8` env failed because I didn't have `flake8` installed locally, but tox installed it in the env automatically. That was a good first win — I didn't have to set anything up manually.

Then I looked at the `py311` env and saw tox spin up a fresh virtualenv under `.tox/py311/`. It installed pytest from the `deps` list in tox.ini and ran `pytest`. My two tests passed in that isolated env. Before today, I'd run pytest globally and occasionally get weird failures when a dependency was missing — tox reproduced the full install in seconds.

I then added a `lint` env that uses `ruff check .` to make sure I wasn't pasting garbage into the repo. Running `tox -e lint` only runs the linter without installing pytest. Running `tox` runs everything in `envlist = lint,py311`.

## Gotcha: local vs. env packages

At one point I got angry because `flake8` was broken in the `lint` env. It turned out I had an old `.pre-commit-config.yaml` cached and tox was reusing the virtualenv. Running `tox -r` forced a recreate — problem gone. Moral of the story: when in doubt, recreate.

## Steps

1. Install tox: `uv tool install tox`
2. Create `tox.ini` with `[testenv]` (deps + commands) and optional named envs like `[testenv:lint]`.
3. Write a simple test file and run `tox`.
4. Run a single env with `tox -e lint`.
5. Run all envs: `tox`.

## What I'd try next

Try `tox -p` to run envs in parallel when the suite grows, and add a `type` env that runs mypy. Also I want to understand the `.tox/` layout better so I can garbage-collect stale envs without nuking the whole directory.
