# Explored rich's Console API — renderables, styles, and output modes

I spent some time playing with rich's Console API today. The `Console` object is the main entry point — you create one and call its methods to print styled output.

**What I tried:**

- `console.print()` — the main way to output things. It accepts any renderable (strings, Text, Panel, Table, etc.) and applies styling.
- `console.log()` — like print but with a timestamp. Good for logging-ish output during development.
- `console.rule("title")` — draws a horizontal line with a centered title. Useful for section breaks.

**Styles:** I tried inline `[bold magenta]text[/]` markup and also passing `Style(color="red", bold=True)` objects. Both work. The markup syntax is shorter for quick things.

**Renderables I tested:**

- `Text("hello", style="green")` — styled plain text.
- `Panel("content", title="Panel Title")` — a bordered box.
- `Table(title="Numbers")` — I added columns and rows. `add_column`, `add_row`, then pass the table to `console.print()`.

**Output modes:** `console.capture()` catches output as a string, useful for tests. The `file` parameter lets you write to a file instead of stdout. I used `record=True` to get the output as SVG later — nice for sharing terminal output.

One thing that caught me: rich uses its own markup syntax that looks like BBCode (`[bold]` / `[/bold]`). It's not ANSI escape codes. You have to use `console.print()`, not the built-in `print()`, to get the rendering.

Overall, the Console API is well-designed. Everything that's renderable can go into `console.print()`, and you can compose complex layouts with Panels containing Tables, etc.
