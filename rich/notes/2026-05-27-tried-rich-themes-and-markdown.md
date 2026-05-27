# Tried rich themes and markdown output

I wanted to see what themes rich ships with and try rendering markdown in the terminal.

Listed available themes with `python -m rich.theme`. There are built-in themes
like `default`, `monokai`, `fruity`, `native`, `vim`, and more. Each one changes
the color palette for syntax highlighting.

I tried rendering markdown:

```python
from rich.console import Console
from rich.markdown import Markdown

md = Markdown("# Hello\n\nThis is **bold** and `code`.")
console = Console()
console.print(md)
```

Markdown renders inline with colors — syntax highlighting for code blocks,
bold/italic rendering, headings in different sizes. Really neat for building
CLI tools that show formatted output.

Tried switching themes by passing `style="monokai"` to Console but that didn't
change the markdown rendering much — I think themes only affect the default
style, not syntax highlighting colors. Need to read more about Theme objects.

Also tried `console.print("[bold red]Hello[/bold red]")` with BBCode-style
markup — that's actually how rich does inline formatting by default. Markdown
is separate.

## What I'd try next

- Look at custom Theme objects with color overrides
- Try nesting markdown in panels or layouts
