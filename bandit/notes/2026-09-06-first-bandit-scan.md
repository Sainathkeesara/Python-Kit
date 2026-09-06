---
last_verified: 2026-09-06
tool_version: "1.9.4"
sources:
  - https://pypi.org/project/bandit/
  - https://bandit.readthedocs.io/en/latest/start.html
---

# Install bandit and run my first scan

> What surprised me about the Python version requirement and the extras.

## The install wall

I tried `pip install bandit` on Python 3.9 and got:

```
ERROR: Package 'bandit' requires a different Python version
```

Turns out bandit 1.9.4 requires Python >=3.10. That's the first thing that tripped me up — I assumed a security linter would support older Pythons since many projects still run 3.9. Had to switch my venv to 3.11 before the install worked.

## The extras trap

After installing, I tried `bandit -f sarif` and got an error about missing SARIF support. bandit ships optional extras per feature: `toml`, `baseline`, `sarif`, `yaml`, `test`. There's no `bandit[all]`. I needed `pip install bandit[sarif,toml]` to get the formatters I wanted.

## First scan

```bash
bandit -r src/ -x tests
```

Ran it on a small Flask app. It immediately flagged an `os.system()` call I'd forgotten about — B601, HIGH severity, HIGH confidence. The output is clear: test ID, severity, confidence, file, line number.

## What surprised me

- `-p` takes **profile names** like `ShellInjection`, not test IDs like `B101`. I kept trying `bandit -p B101` and getting nothing. The flag to skip specific tests is `-s`, not `-p`.
- Default exclusions don't include `venv/` or `.venv/`. I had to add `-x .venv,venv` manually or bandit would scan my entire virtual environment.
- `uv` install was smoother than `pip` — avoids PyYAML build failures that still plague bare pip on some Python 3.11/3.12 environments.

## What I'll try next

I want to build a baseline file so I can track new findings over time, then wire bandit into a pre-commit hook.
