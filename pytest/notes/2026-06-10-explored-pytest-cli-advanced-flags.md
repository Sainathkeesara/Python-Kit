# 2026-06-10-explored-pytest-cli-advanced-flags.md

Today I tried out the `pytest --co`, `--collect-only`, and `--fixtures` flags on a small test file.

## --collect-only

```
pytest --collect-only
```

This lists all tests pytest finds without running them. It counted my three test functions and showed their file paths. Useful when I want to see what's available before committing to a run.

## --fixtures

```
pytest --fixtures
```

This printed a huge list of built-in fixtures like `tmp_path`, `capsys`, `monkeypatch`. I scrolled through and tried `tmp_path` in a test to see a disposable temp directory. It cleaned up automatically.

## --co

```
pytest --co
```

This seems to be a short alias for `--collect-only` — same output, same count. I ran both and they matched exactly.

## What I'd try next

I want to see what `--collect-only -q` does, and try `pytest --fixtures-per-test` if it exists in my version.
