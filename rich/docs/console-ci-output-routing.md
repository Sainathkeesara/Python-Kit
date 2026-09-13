---
last_verified: 2026-09-13
tool_version: n/a
---

# Rich Console in practice: output routing, force_terminal, and NO_COLOR for CI and local dev

## Purpose

Rich detects whether stdout is a real terminal and adjusts its behavior accordingly — colors, panels, and progress bars render interactively in a TTY but degrade to plain text in CI logs or piped output. This doc covers three practical knobs that control that behavior: output routing (sending Rich output to files, stderr, or in-memory buffers), `force_terminal` (overriding TTY detection), and `NO_COLOR` (respecting the community standard for disabling color). These settings matter when the same CLI tool needs to look good on a developer's laptop and produce parseable output in a GitHub Actions log.

## When to use

- Your CLI tool uses Rich for styled output and needs to work in both interactive terminals and CI pipelines.
- You want to capture Rich output as a string for testing, logging, or writing to a file.
- You need to enforce or respect the `NO_COLOR` convention across your tool chain.
- You are writing a script that pipes Rich output into another tool (`jq`, `grep`, etc.) and needs raw text without escape codes.

## Prerequisites

- Rich installed (`pip install rich` or `uv add rich`).
- Python 3.9 or newer.
- Basic familiarity with `Console` and `console.print()`.

## Output routing

A `Console` instance targets a file-like object. The default is `sys.stdout`, but you can point it anywhere:

```python
# last_verified: 2026-09-13 · rich n/a
import io
from rich.console import Console

# Route to a StringIO buffer for testing or logging
buf = io.StringIO()
console = Console(file=buf, no_color=True)
console.print("[bold green]Pass[/bold green]")
captured = buf.getvalue()  # "Pass\n" — no ANSI escapes

# Route to stderr while stdout stays clean
err_console = Console(file=sys.stderr)
err_console.print("[red]Warning:[/red] disk full")
```

The `file` parameter accepts any object with a `write(str)` method. Combined with `no_color=True` or `force_terminal=False`, this lets you capture styled output as plain text for assertions in tests or for writing structured logs.

## `force_terminal`

By default, Rich checks `sys.stdout.isatty()` to decide whether to emit ANSI codes. `force_terminal` overrides that check:

```python
# last_verified: 2026-09-13 · rich n/a
import sys
from rich.console import Console

# Force terminal mode even when piped or in CI
console = Console(force_terminal=True)
console.print("[bold blue]This will have ANSI codes[/bold blue]")

# Force non-terminal mode even in a real TTY
console = Console(force_terminal=False)
console.print("[bold blue]This will be plain text[/bold blue]")
```

Common scenarios:

| Scenario | `force_terminal` | Effect |
|---|---|---|
| Local dev in a real TTY | `None` (default) | Rich detects TTY, enables colors and panels |
| CI pipeline (GitHub Actions) | `True` | Forces ANSI output so logs contain styled text |
| Piped to `jq` or `grep` | `False` | Strips styling for clean downstream parsing |
| Test capture with `capsys` | `False` | Plain text assertions without escape codes |

In CI, setting `force_terminal=True` on the console ensures that GitHub Actions log output retains colors and formatting, making it easier to scan failures. If you need machine-readable output, set `force_terminal=False` or redirect to a `StringIO`.

## `NO_COLOR`

The `NO_COLOR` convention says: when an environment variable named `NO_COLOR` is set (to any value), command-line software should not emit ANSI color escape codes. Rich respects this automatically:

```python
# If NO_COLOR is set in the environment:
#   console.print("[red]Hello[/red]")  →  "Hello" (no ANSI codes)
# If NO_COLOR is not set:
#   console.print("[red]Hello[/red]")  →  "\033[31mHello\033[0m"
```

You can also control this programmatically:

```python
from rich.console import Console

# Explicitly disable color regardless of environment
console = Console(no_color=True)

# Explicitly enable color regardless of environment
console = Console(color_system="truecolor")
```

When `no_color=True` is passed to the constructor, it takes precedence over the `NO_COLOR` environment variable. This is useful for testing: you can force color on or off regardless of the developer's shell settings.

## Putting it together: a CI-friendly CLI pattern

A typical pattern for a CLI tool that works in both local dev and CI:

```python
# last_verified: 2026-09-13 · rich n/a
import os
import sys
from rich.console import Console

def make_console() -> Console:
    """Build a Console that respects CI and NO_COLOR conventions."""
    if not sys.stdout.isatty() and not os.environ.get("CI"):
        # Piped or non-interactive: plain text
        return Console(force_terminal=False, no_color=True)
    # Interactive terminal or CI: styled output
    return Console(force_terminal=bool(os.environ.get("CI")))

console = make_console()
console.print("[bold green]Deployment[/bold green] complete.")
```

This pattern:
1. Detects whether stdout is a TTY.
2. Checks for the `CI` environment variable (set by GitHub Actions, GitLab CI, etc.).
3. Falls back to plain text when piped, or forces styled output in CI.
4. Respects `NO_COLOR` automatically (Rich reads it unless you override `no_color`).

## Verify

1. Run a Rich-styled script in a real terminal — colors and panels should appear.
2. Pipe the same script to `cat` — output should be plain text without ANSI codes.
3. Set `NO_COLOR=1` and run again — colors should disappear even in a TTY.
4. In a GitHub Actions step, set `force_terminal=True` — the log should show colored output.
5. Capture `Console(file=StringIO(), no_color=True)` output and assert it contains no `\033` escape sequences.

## Common errors

- **Colors appear in CI logs when they shouldn't.** CI runners typically do not have a TTY, but if `force_terminal=True` is set globally, ANSI codes leak into logs. Check whether your `Console` constructor passes `force_terminal` conditionally.
- **`NO_COLOR` is set but colors still appear.** If `Console(no_color=False)` is passed explicitly, it overrides the environment variable. Remove the explicit `no_color` parameter to let the environment variable take effect.
- **Test assertions fail on ANSI escape sequences.** When capturing Rich output for assertions, always create the `Console` with `no_color=True` and `file=io.StringIO()`. This strips styling before the string reaches your assertion.
- **`force_terminal=True` breaks downstream tools.** If you pipe Rich output to `jq` or `grep`, `force_terminal=True` injects escape codes that break parsing. Use `force_terminal=False` or redirect to a file with `no_color=True`.
