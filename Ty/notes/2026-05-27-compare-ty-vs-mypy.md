# Ty vs mypy — first impressions

I installed both Ty and mypy through uv to see how they compare for type checking a simple script.

Both found the same basic errors — missing return type on a function, passing `int` where `str` was expected. No surprises there.

What stood out:

- **Speed.** Ty felt noticeably faster. On a small file with three functions, Ty was instant; mypy took maybe half a second. Not a big deal now, but I bet it matters on a big project.
- **Output.** Ty's error messages are shorter — almost terse. mypy gives you more context (expected type, actual type, line number with snippet). For a beginner, mypy's output is friendlier.
- **Setup.** Ty needed zero config to work. mypy has sensible defaults too, but the docs immediately point you to `pyproject.toml` settings. Ty feels like it wants to be drop-in.
- **Strict mode.** I tried `mypy --strict` and got a wall of warnings about missing annotations everywhere. Ty doesn't have a `--strict` flag in the same way — it just checks what you annotated.

For now, I'll use Ty day-to-day because it's fast and minimal. I'll keep mypy around for CI where I want the stricter checks.
