# Tried the official mypy quickstart — gradual typing and strict mode

I followed the mypy docs quickstart from start to finish today. I'd poked at mypy before but never done the intended onboarding path — gradual typing first, then strict mode.

## Step-by-step

The quickstart opens with a bare Python function — no types at all:

```python
def add(a, b):
    return a + b
```

Running `mypy program.py` produces zero output. That caught me off guard — I expected an error or at least a warning. The whole point is gradual typing: mypy says nothing about untyped code unless you ask it to. You opt in file by file.

Then they add annotations:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Now `mypy` will flag `add("x", 2)` as a type error downstream. This clicked for me — the value prop isn't checking the function itself, it's catching mismatched callers.

## Trying on a mixed file

I wrote a module with typed and untyped functions together:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def repeat(s, n):  # untyped
    return s * n
```

Running `mypy --strict` on this gave errors for every untyped parameter. Running without flags only flagged callers of `repeat` where the inferred type was used wrong. The difference was dramatic.

The quickstart also introduces `reveal_type()` — a mypy-only function that prints what mypy thinks a variable's type is at that point:

```python
reveal_type(repeat("hi", 3))  # mypy prints: Revealed type is "builtins.str"
```

It doesn't exist at runtime though. First time I ran the file with Python I got a `NameError`. Need to strip these calls before executing.

## Got stuck on

- **strict vs --strict confusion.** I put `strict = True` in pyproject.toml under `[tool.mypy]` — nope, that syntax didn't work. Turns out it goes under plain `[mypy]` in a `.ini` config, or `strict = true` in `mypy.ini`. Took me three tries.
- **`reveal_type` is debug-only.** Great for understanding inference, but you must remove the calls before running with Python. Easy to forget.
- **Strict is all-or-nothing per run.** Passing `mypy --strict src/` hits every file under `src/`. I expected it to only flag new violations — nope, every untyped function everywhere. I ended up using `--strict` on individual files to avoid drowning in errors.

## What I'd try next

Set up per-module overrides in the config file so `disallow_untyped_defs` is off for test files and on for source. Also want to try `--new-semantic-analyzer` since the docs mention it's now default but I'm not sure my version has it.
