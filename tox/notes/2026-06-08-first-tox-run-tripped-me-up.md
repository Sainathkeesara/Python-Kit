# First tox run — what tripped me up

> My scratch notes after running tox for the first time. Not a polished guide.

Ran `tox -e py311` and it worked. Then I edited `tox.ini` to point at my src layout tests and it broke.

Turns out tox defaults to installing your *entire project* into the test env (because `package = wheels` assumes you have a setup.py/pyproject.toml with a `[project]` table). My package only had a `src/` layout, so tox tried to build it and failed. I had to add `package = src` under `[testenv]` so it knows where to look.

I also got confused by `--rootdir`. pytest defaults to the current working directory, which worked when I ran `tox -e py311` from the repo root, but failed when I ran `tox -e py311` from a subdirectory. I ended up adding `--rootdir = {toxinidir}` in pytest addopts.

Forgetting `skip_install = true` in my lint env caused tox to try to build the package every time I ran lint. The lint env was supposed to just run `ruff check .`, so that was a waste of a minute debugging ugly build errors.

Using `tox -e py311` works even if `envlist` in `[tox]` lists other envs — you don't have to run them all. That saves time.

And `setenv = PYTHONPATH = {toxinidir}/src` in tox.ini fixed another error where pytest couldn't find my modules. I had to repeat that for every env, which felt clunky, so I put it under `[testenv]` to apply to all of them by default.

Worth knowing: tox prints coloring weirdly inside nested emulators. Try `--no-color` if the output looks like garbage.
