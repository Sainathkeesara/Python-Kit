# Followed the official mypy quickstart — gradual typing and strict mode

I went through the mypy docs quickstart today. I'd already run mypy a few times, but I wanted to follow the actual intended onboarding path — gradual typing, then strict mode — instead of just throwing `--strict` at everything.

## Following the quickstart steps

The quickstart starts with a plain Python function and runs mypy. It passes because untyped code is valid — mypy won't complain unless you ask it to.

```python
def add(a, b):
    return a + b
```

Running `mypy program.py` on this prints nothing. That's the gradual part — you opt in.

Then they add annotations:

```python
def add(a: int, b: int) -> int:
    return a + b
```

mypy now knows the types and will catch someone passing `add("x", 2)` downstream.

## Trying gradual typing on a real-ish file

I created a small module with a mix of typed and untyped functions:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def repeat(s, n):  # deliberately untyped
    return s * n
```

Running `mypy` with no flags: only the callers of untyped functions get checked for consistency with what mypy can infer. `repeat` itself is a no-check zone.

The quickstart suggests running `reveal_type()` in the code to see what mypy infers. I added `reveal_type(repeat("hi", 3))` and mypy printed `Revealed type is "builtins.str"`. That's handy for debugging why something isn't failing.

## Enabling strict mode

When I added `--strict` the error count jumped fast:

- Missing type annotations on every untyped parameter and return
- Missing annotations on module-level variables
- Implicit `Any` in function bodies

Worth doing on a per-file basis first. `mypy --strict src/core.py` catches everything in that file without flooding me with errors from the whole project.

## Where I got stuck

- **The quickstart doesn't say you need `--strict` in the config file, not `--strict` on the CLI.** I put `strict = true` under `[mypy]` in pyproject.toml and it worked. But if you use the `--strict` flag with a config that has `strict = false`, the flag wins — that tripped me up for a minute.
- **`reveal_type()` is a special mypy-only function.** It doesn't exist at runtime. Your IDE will flag it as undefined. I had to remember to remove the calls before running the file with Python — `NameError` otherwise.
- **Strict mode applies to ALL files in the run.** If you pass a directory to `mypy --strict src/`, it checks every file under it strictly. I expected "strict" to mean "warnings as errors" but it actually means "require annotations everywhere". I had to use `exclude` or `per-module overrides` to keep old code passing.

## What I'd try next

- Set up `per-module overrides` in the config so I can turn `disallow_untyped_defs` off for test files while keeping it on for source.
- Try `--new-semantic-analyzer` — the quickstart mentions it's the default in newer versions but I haven't tested the difference.
- Configure my editor to run mypy on save with the strict profile only on the current file, so I don't get project-wide noise on every edit.
