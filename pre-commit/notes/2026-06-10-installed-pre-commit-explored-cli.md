# 2026-06-10-installed-pre-commit-explored-cli.md

I installed pre-commit with `pip install pre-commit` and ran `pre-commit --help` to see what subcommands are available.

## What the CLI offers

```
pre-commit install
pre-commit run --all-files
pre-commit run-hooks
pre-commit sample-config
pre-commit validate-config
pre-commit autoupdate
pre-commit clean
pre-commit gc
```

Most of these I don't need yet. The ones that stood out:
- `sample-config` — spits a boilerplate `.pre-commit-config.yaml` so I don't start from zero.
- `validate-config` — checks syntax without touching any hooks.
- `autoupdate` — bumps the versions of repos in the config. I ran it and it told me which hooks had newer tags available.

I also tried `pre-commit help run` and saw flags like `--verbose`, `--color`, and `--show-diff-on-failure`.

## What tripped me up

`pre-commit install` failed silently once because I was in the wrong directory — it only looks for `.pre-commit-config.yaml` in the current folder. The `sample-config` command helped me bootstrap without guessing.
