# First mypy run

I installed mypy with `uv add mypy` and wrote a tiny annotated function:

```python
# demo.py
def add(a: int, b: int) -> int:
    return a + b

result = add("1", "2")
print(result)
```

Ran `mypy demo.py` and got:

```
demo.py:5: error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

Fixed it by calling `add(1, 2)`. Second run had no output — clean.

Then I tried a None check:

```python
def get_name(user: dict | None) -> str:
    if user is None:
        return "unknown"
    return user["name"]
```

mypy passed this without complaints because I handled the None case.

I also tried `reveal_type()`:

```python
reveal_type(result)
```

mypy printed the inferred type at that point. Handy for debugging.

Next I'll try the `--strict` flag and see what else it catches.
