# uv: creating and exploring a virtual environment

Today I followed up on the uv primer and actually tried creating a virtual environment. Here's what I did.

**Creating the environment.** I ran `uv venv .venv` inside an empty project folder. It created a `.venv` directory almost instantly — way faster than `python -m venv .venv` usually is. No output except a path telling me where it landed.

**Activating it.** Then I ran `source .venv/bin/activate`. The prompt changed to show `(.venv)` at the front — same as any other venv.

**Checking what's inside.** `uv pip list` showed only `pip` and `setuptools` by default. I added a package with `uv add requests`, and it showed up along with its dependencies (`urllib3`, `certifi`, etc.).

**What I noticed.** The speed difference is real — `uv add requests` finished before I could blink. The lockfile `uv.lock` appeared in my project root, and I could see it pinned exact versions.

**One thing that tripped me up.** I forgot to activate the venv before running `uv add`, so it created a `pyproject.toml` but I wasn't sure which environment it installed into. Turns out `uv add` works regardless of whether the venv is active — it reads `.venv/` by convention.

Next I want to try `uv sync` on a project with a pre-existing `pyproject.toml`.
