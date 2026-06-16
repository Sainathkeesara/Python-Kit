# Explored Ty CLI flags and output formats

I ran `ty --help` to see what subcommands exist. There's `check`, `run`, and `config` — that's it. Simple.

`ty check --help` showed the flags. A few that stood out:

- `--show-column-numbers` — adds column to error output. Without it you only get line numbers.
- `--exclude` — skip files/dirs. I passed `--exclude '.venv'` to avoid noise.
- `--ignore-none-return` — doesn't complain when a function with no return hits a bare return. I hit this with some old code.
- `--python-version` — set the Python version for checks. Defaults to whatever's running.

Output format is plain text by default — errors look like `error[file:line:col]: message`. No JSON or machine-readable output that I could find.

Compared to mypy, Ty has fewer flags. mypy has `--strict`, `--disallow-untyped-defs`, `--ignore-missing-imports` that don't have direct Ty equivalents. Ty feels more "check what you wrote, don't guess about the rest." mypy's `--strict` mode is way more opinionated.

I also tried `ty run` — it runs a Python file with type checking in realtime. Kinda like `python -m pdb` but for types. Didn't expect that.

What I'd try next: figure out if there's a way to output errors in a format CI tools can parse. The plain text is fine for terminal but I'd want something structured for GitHub Actions annotations.
