# tox first run notes

Ran `tox --version` to make sure it was installed — got `4.25.0`. Then I looked at what envs I had defined by running `tox list`, but I hadn't created a `tox.ini` yet, so it told me there was no config. Oops, order of operations.

Created a minimal `tox.ini` with one `py311` env and a single deps on pytest. Made a throwaway `test_math.py` with a passing test.

Ran plain `tox` — it built the env, installed pytest into `.tox/py311/`, and executed the test. Output was clean. Then I ran `tox -e py311 -- pytest -v` to pass args through to pytest and got verbose output.

I tripped up on the env list command syntax. I expected `tox envs list` because the help text mentions `envlist`, but the actual subcommand is `tox list` (or `tox -l`). The help screen does show it, but I missed it the first time.

Also worth noting: tox rebuilds the env from scratch whenever you change deps. When I added a second deps entry, the next `tox` run wiped and recreated `.tox/py311/`. That's by design — reproducibility over speed.

## What worked

- `tox --list-envs` showed my single env
- `tox -e py311` ran just that env
- Passing flags through with `--` worked fine

## What tripped me up

- Thought `tox env list` was a command (`tox list` is correct)
- Forgot to `cd` into the project root first and got "no tox.ini found" twice

## What I'd try next

- Add a second env for a different Python version
- Add a lint env that runs ruff or flake8
- Figure out the `tox -e py311 -- recreate` flag
