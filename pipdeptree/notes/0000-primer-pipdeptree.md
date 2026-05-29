# pipdeptree — quick primer

> First-day notes for someone who's never used pipdeptree. Personal voice, plain language.

## What is it?

pipdeptree is a CLI tool that shows your Python package dependencies as a tree — think `npm ls` or `cargo tree` but for pip-installed packages. It reads what's installed in your environment and prints a hierarchy of "who depends on who."

I'd compare it to `pip list` on steroids: `pip list` just shows flat names and versions, while pipdeptree shows the parent-child relationships between packages. If you've ever wondered "what actually requires this transitive dependency?", pipdeptree answers that.

## What does it do?

You run `pipdeptree` in your terminal and it prints a tree of installed packages, showing top-level packages and their dependencies underneath. It also flags dependency conflicts (when two packages need different versions of the same thing). It can output JSON for machine parsing, and you can tell it to only show packages you explicitly installed (the `--packages` flag filters by name).

## Why does it exist?

When you work with Python long enough, you end up with a tangle of packages that pip pulled in as dependencies of other packages. If you just run `pip list`, you see everything — including things you never asked for. pipdeptree makes it obvious which packages are "top-level" (things you installed on purpose) and which are transitive (brought in by something else). This matters when you're trying to slim down a project, debug a version conflict, or figure out if you can safely remove a package.

Before pipdeptree, you'd manually trace `pip show <package>` for each dependency or dig through `METADATA` files in site-packages. Not fun.

## Key terminology

- **Top-level package** — A package you installed directly (e.g., `pip install requests`). Example: `requests` shows at the root of the tree.
- **Dependency / transitive dependency** — A package installed because something else needs it. Example: `urllib3` shows up indented under `requests`.
- **Dependency conflict** — When two packages require incompatible versions of the same third package. Example: pipdeptree prints a `** Conflict **` block.
- **`--packages`** — Filter to show only certain packages and their sub-trees. Example: `pipdeptree --packages requests`.
- **`--json`** — Output the tree as JSON instead of the default text tree. Example: `pipdeptree --json`.
- **`--warn`** — Control warning output (e.g., about missing packages). Example: `pipdeptree --warn silence`.
- **`pip freeze`** — Flat list of all packages with versions (often confused with pipdeptree). Example: `pip freeze > requirements.txt`.

## A tiny example

```bash
pip install pipdeptree
pipdeptree
```

This installs pipdeptree and prints the full dependency tree for the current environment. The output looks like a directory tree with arrows showing which package requires which.

## What I'll cover next

I want to run pipdeptree on this project to see our actual dependency tree, then try the JSON output to understand the structure programmatically. After that I'll figure out how to separate top-level deps from transitive ones for a cleaner requirements file.
