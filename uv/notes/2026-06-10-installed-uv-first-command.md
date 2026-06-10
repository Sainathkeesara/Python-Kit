# Installed uv and ran my first commands

I finally installed uv today. Used the shell script from the docs:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

It printed something about adding `~/.cargo/bin` to my PATH. I had to open a new terminal for `uv` to be found.

First thing I ran was `uv --version` — got `uv 0.4.x` or something, can't remember the exact patch. Then `uv help` showed a wall of subcommands. Way more than I expected — `uv add`, `uv sync`, `uv run`, `uv tool`, `uv python`, `uv pip`, etc.

Next I tried `uv run` on a script with inline metadata (PEP 723). Created a one-liner that just printed `"hello from uv"`, ran `uv run hello.py`, and uv created an ephemeral venv and ran it instantly.

No errors, which was nice. The speed difference from pip is real — `uv run` felt instant even on first run when it had to set up the venv.
