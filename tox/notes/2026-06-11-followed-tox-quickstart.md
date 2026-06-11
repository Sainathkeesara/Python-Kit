# Followed the tox quickstart — multi-env setup

I followed the official tox quickstart today to set up a project with multiple
test environments. The goal: run pytest in one env and ruff lint in another,
without them stepping on each other.

## Steps

1. Installed tox with `uv tool install tox` — came back as a `tox` command.
2. Created a `tox.ini` with two envs in `envlist`: `lint, py311`.
3. Added `[testenv:lint]` with `deps = ruff` and `commands = ruff check .`.
4. Added `[testenv]` base config with `deps = pytest` and `commands = pytest`.
5. Ran `tox` — it created `.tox/lint/` and `.tox/py311/`, installed deps, ran
   both suites.

First run passed. Both envs ran sequentially. The output showed a clear
pass/fail per env, which I liked — one failure doesn't abort the rest.

## What tripped me up

### `skip_install` on lint

The quickstart mentions that tox tries to build your package by default. My
project doesn't have a `pyproject.toml` build table yet, so the lint env
failed with a build error. I had to add `skip_install = true` under
`[testenv:lint]` — the linter doesn't need the package installed.

### `.tox/` eats disk

After two runs I noticed `.tox/` was already 20 MB. Each env is a full
virtualenv. That's fine locally, but I can see it getting out of hand on a
project with many Python versions. I added `.tox/` to `.gitignore`.

### Factor env syntax

I tried `tox -e py311,lint` to run both but it recreated both from scratch. I
expected it to reuse the cached envs. Turned out `-r` forces recreate, and
without it tox does reuse — my first run was fine so it didn't need to
recreate. The second run recreated because I changed the config between runs.
That's tox working as designed, but it surprised me.

### `commands` order matters

I put `ruff check .` before `pytest` in the base `[testenv]` and lint ran
before tests. That's fine for `tox`, but `tox -e py311` still ran both
commands in the py311 env. I split lint into its own env to keep things
clean.

## What I'd try next

I want to add a `mypy` env and see how tox handles three envs. Also curious
about `tox -p` for parallel runs — the quickstart mentions it but I didn't
try it today. And I should look into `generative envlist` so I don't have to
list every Python version manually.
