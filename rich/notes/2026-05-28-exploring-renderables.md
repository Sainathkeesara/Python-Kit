# Exploring Rich renderables

Started messing with Rich's renderable types. Tried tables, panels, layouts, and the markup syntax.

**Tables** — `Table` is surprisingly flexible. You add_column with styles, add_row with values. Works like a HTML `<table>` but in the terminal. I passed `title=` to give it a header.

**Panels** — `Panel` wraps any renderable in a box with an optional title. I nested a table inside a panel and it rendered fine. Feels like a `<div>` with a border.

**Layouts** — `Layout` splits the terminal into regions. Tried a header-body-footer split. Took me a few tries to get the ratios right — had to specify `size=` or `ratio=` or it would collapse.

**Markup** — Rich uses `[bold]` / `[red]` tags inside strings. Looks like BBCode. Works in `console.print()` but not in regular `print()`. Easy to forget that.

Got stuck on nesting layouts — the inner layout didn't respect the parent's boundaries on first try. Fixed by setting `minimum_size=` explicitly.

What I'd try next: use `rich.inspect()` on a dict to see how deep the introspection goes, and try `rich.pretty.pprint` for data dumping.
