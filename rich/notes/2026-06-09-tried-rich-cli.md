# Tried the rich CLI — what console features export to terminal

I installed rich and discovered it has a CLI too. Running `python -m rich` shows the help — turns out there's a bunch of built-in demos and utilities built into the library itself.

## What I found

`python -m rich` with no args drops into an interactive pager showing a styled rich repr of all the available subcommands. The main ones I played with:

- `python -m rich.text` — Renders styled text with markup. I tried `python -m rich.text "Hello [bold red]World[/]"` and it printed the formatted output directly to the terminal.
- `python -m rich.inspect` — Inspects any Python object. `python -m rich.inspect rich.console.Console` dumped all attributes and methods in a tree panel.
- `python -m rich.markdown` — Renders a markdown file as styled terminal output. I piped a README through it and got formatted headings, lists, and code blocks.
- `python -m rich.table` — Shows a demo table. Helpful for seeing what's possible.
- `python -m rich.syntax` — Syntax-highlights a source file. I pointed it at a Python file and got colored output without needing pygments.
- `python -m rich.tree` — Draws tree structures. Good for directory layouts.
- `python -m rich.rule` — Prints a horizontal rule across the terminal.

## What surprised me

I didn't expect the CLI to be this useful. The `markdown` and `syntax` subcommands are basically mini tools on their own — I could see using `python -m rich.syntax myfile.py | less -R` as a quick syntax highlighter in a pipeline.

The output auto-detects terminal width and wraps content, which most ad-hoc formatters don't bother with.

## What I'd try next

I want to use `python -m rich.markdown` in a shell pipeline that processes README files, and maybe combine `rich.inspect` with a script that explores third-party modules.
