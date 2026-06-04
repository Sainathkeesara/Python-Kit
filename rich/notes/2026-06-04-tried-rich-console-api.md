# Tried Rich's console API

I installed rich with `uv add rich` and started poking at the Console class.

`print()` — works like the built-in but supports markup. I ran:

```python
from rich import print
print("[bold green]Hello[/] from rich")
```

That's already way nicer than plain print.

`print_json()` — I passed a JSON string and it syntax-highlights the output:

```python
from rich import print_json
print_json('{"name": "Alice", "scores": [90, 85]}')
```

Keys are one color, values another, and it auto-indents. Good for debugging API responses.

`rule()` — draws a horizontal line with an optional label:

```python
from rich.console import Console
console = Console()
console.rule("[bold]Section Header[/]")
```

Prints a full-width divider line. I used it to separate sections in my output.

Console also has a `log()` method that timestamps output. That was a surprise — I thought it'd be more complicated. Just `console.log("done loading")` and you get a timestamped line.

`separator` — I don't think there's a separate `separator` method. The closest is `rule()`. Maybe I'll find more under `Console` methods later.

Next I want to try tables and progress bars.
