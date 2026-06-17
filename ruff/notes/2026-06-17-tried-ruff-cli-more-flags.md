# Tried more Ruff CLI flags today

I already knew `ruff check` and `ruff format`, but today I poked at the less common flags.

## --show-settings and --show-files

These two tell you what Ruff *thinks* it's doing:

```bash
ruff check --show-settings src/
```

This dumps every resolved config option — which rules are enabled, what `exclude` patterns it uses, what `target-version` it picked up from pyproject.toml. Helpful when a rule isn't firing and you can't figure out why.

```bash
ruff check --show-files src/
```

Lists every file Ruff plans to check, respecting the `exclude` and `extend-exclude` settings. I used this to confirm `.venv/` was being skipped.

## --add-noqa

```bash
ruff check --add-noqa src/
```

Scans the codebase and inserts `# noqa` comments on lines that currently have violations. I don't use this often but it's useful when I want to freeze existing issues and only catch new ones.

## --statistics

```bash
ruff check --statistics src/
```

Instead of listing every violation, it just counts them — grouped by rule code. Good for tracking whether a codebase is getting cleaner over time without wading through the full output.

## ruff rule

```bash
ruff rule SIM105
```

Prints the full documentation for a rule — what it does, what the fix looks like, what's unsafe about it. I use this way more than I expected when I'm deciding whether to enable a new rule.

## What surprised me

- `--show-settings` also prints the *source* of each setting (`pyproject.toml`, `ruff.toml`, CLI flag). Saved me from hunting through config files.
- `ruff rule` works offline — no network call. The docs are baked into the binary.
