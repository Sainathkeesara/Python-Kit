# Trying mypy CLI flags

I installed mypy with `uv add --dev mypy` and ran it against the broken file I made. Here's what each flag did.

## `mypy tried-mypy-first-check.py` (default)

Caught 4 errors — type mismatches for `add` args, `result` assignment, the `str` in the list, and the missing `age` attribute. Good baseline.

## `--strict`

This turned on everything: `--check-untyped-defs`, `--disallow-any-expr`, `--disallow-any-generics`, `--warn-return-any`, and more. My file went from 4 errors to 9 — it complained about the untyped `print` calls too. Feels like `--strict` is for projects that are fully typed from day one.

## `--check-untyped-defs`

Didn't change anything for my file since all my functions were already annotated. I'd need a file with bare `def foo():` to see it in action.

## `--ignore-missing-imports`

No effect either since I wasn't importing any third-party libs. Good to know it exists — I can see this being useful when you depend on a package that doesn't have stubs.

## `--disallow-untyped-defs`

Still no change because I already typed all the defs. I should make a file with untyped functions to test this and `--check-untyped-defs` properly.

Next time I want to try `reveal_type()` in the middle of a function and see what mypy prints.
