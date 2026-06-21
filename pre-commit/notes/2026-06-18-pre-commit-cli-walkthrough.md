# Installed pre-commit and walked through the CLI

I ran `pip install pre-commit` and then started poking at what commands are available.

## First look

`pre-commit --help` lists the subcommands. The ones that stood out:

- `install` — sets up the git hook. I ran it, and it created `.git/hooks/pre-commit`.
- `run` — runs hooks. I tried `pre-commit run --all-files` and it skipped everything because I hadn't configured anything yet.
- `sample-config` — prints a starter `.pre-commit-config.yaml`. I redirected it to a file: `pre-commit sample-config > .pre-commit-config.yaml`. Good starting point.
- `validate-config` — checks the syntax. I ran it after editing my config and it caught a stray tab.
- `autoupdate` — bumps hook versions. It looked at the repos in my config and printed newer tags.
- `clean` — removes cached hook repos from `~/.cache/pre-commit/`.

## Digging into `run`

`pre-commit help run` shows flags:
- `--verbose` — prints what each hook is doing
- `--show-diff-on-failure` — shows the diff if a hook modifies files
- `--color` — I turned this on for readability
- `--from-ref` / `--to-ref` — run on a specific range of commits

I tried `pre-commit run --verbose` with a ruff hook. It showed each file being checked and the exit code.

## What caught me

`pre-commit install` only looks for `.pre-commit-config.yaml` in the current directory. I was in a subfolder and it told me nothing was configured — no error, just a warning in the output. Took me a minute to figure out I needed to run it from the repo root.

Also `autoupdate` modifies the config file in place — it updates the `rev` fields and writes back without asking.
