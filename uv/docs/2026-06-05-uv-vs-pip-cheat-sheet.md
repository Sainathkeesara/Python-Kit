# uv vs pip — what I learned mapping commands

I spent an afternoon translating my usual pip workflow into uv commands. Here's
the cheat-sheet I wish I'd had.

## The mapping I use daily

| You want to… | pip | uv |
|---|---|---|
| Install a package | `pip install requests` | `uv pip install requests` |
| Install from requirements | `pip install -r reqs.txt` | `uv pip install -r reqs.txt` |
| Freeze installed packages | `pip freeze` | `uv pip freeze` |
| List installed | `pip list` | `uv pip list` |
| Uninstall | `pip uninstall requests` | `uv pip uninstall requests` |
| Show package details | `pip show requests` | `uv pip show requests` |
| Check deps | `pip check` | `uv pip check` |
| Search (removed from pip) | `pip search flask` | `uv pip search flask` |

`uv pip` subcommands intentionally mirror pip's CLI, so muscle memory mostly
transfers. The big difference is speed — uv feels instant for most operations.

## Where uv broke my habits

**1. `uv pip install` without an active venv.**
With pip I'd always `source .venv/bin/activate` first. With uv you don't need
to — `uv pip install` creates a `.venv` automatically if one isn't found. That
tripped me up the first time because I thought it failed silently (it didn't).
I got confused when my system Python couldn't import what uv had installed.
Turns out uv had created its own `.venv` in the project root. Running
`uv pip install --system` bypasses this, but the docs recommend sticking with
per-project venvs.

**2. No `pip install --editable` syntax collisions.**
`uv pip install -e .` works the same as pip's editable install. No surprise
there, but I kept writing `uv pip install --editable .` out of habit and it
worked fine.

**3. `uv pip compile` — pip doesn't have this.**
Pip has no built-in lockfile. `uv pip compile reqs.in > reqs.txt` generates a
pinned requirements file from loose dependencies. I tried it on a project with
just `requests>=2.28` and got a full tree of pinned transitive deps. It's like
having `pip freeze` but before you install anything.

**4. `uv pip sync` is my new favourite command.**
`uv pip sync reqs.txt` installs exactly what's in the file, removing anything
extra. I'd been doing `pip install -r reqs.txt && pip freeze | cut ...` to
achieve the same thing. `sync` does it in one step.

## What I'd try next

I want to see how `uv pip compile` handles conflicting transitive deps, and
whether `uv pip sync` is safe to run in CI without a fresh venv every time.
Also curious if `uv pip install --index-url private-repo` works as smoothly
as pip's `--extra-index-url`.
