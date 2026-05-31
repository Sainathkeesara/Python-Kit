# tox CLI first run

Tried tox today. First ran `tox --version` to confirm it was installed — got 4.25.0. Then `tox list` to see what envs I had. Oops, no `tox.ini` yet, so it complained. Should have made the config first.

Made a minimal `tox.ini` with one `py311` env and pytest as deps. Created a quick `test_math.py` with a passing test.

Ran plain `tox` — it built the env, installed pytest into `.tox/py311/`, and the test passed. Then tried `tox -e py311 -- pytest -v` to pass args through. Worked nicely.

Got confused on the env list syntax. Expected `tox env list` because the help mentions `envlist`, but it's actually `tox list` (or `tox -l`). Missed that on first read of help.

When I added a second deps entry, tox wiped and recreated the whole env. That's expected — it prioritizes reproducibility over speed.

What worked:
- `tox --list-envs` showed my env
- `tox -e py311` ran just that one
- Flags passed through with `--` worked

What tripped me up:
- Thought `tox env list` was a command
- Forgot to `cd` into project root and got "no tox.ini found" twice

Next: adding a second env for different Python version and a lint env.