# Typer — quick primer

> First-day notes for someone who's never used Typer. Personal voice, plain language.

## What is it?

Typer is a Python library for building CLI applications. If you've used argparse or click, it's the same problem space — you define commands and options, and Typer generates a CLI for you. The difference is Typer uses Python type hints to declare arguments instead of decorators with strings. This means your IDE can autocomplete and validate your CLI definitions, and you get automatic help text generation.

## What does it do?

It lets you define CLI commands as regular Python functions and automatically handles argument parsing, validation, and help text. You annotate function parameters with types (str, int, bool, list, etc.) and Typer builds a fully-featured CLI with `--help` support out of the box. It also generates shell completion scripts for bash, zsh, and fish.

## Why does it exist?

Before Typer, CLI frameworks like argparse required you to declare arguments in a separate block of code, far from the function that used them. Click improved this with decorators, but Typer takes it further by using type hints — the same hints you'd add for mypy or IDE support anyway. This means less boilerplate and more self-documenting code. It's especially useful for tools that need to expose Python functionality to the command line.

## Key terminology

- **Command** — A function decorated with `@app.command()` that becomes a CLI subcommand. Example: `@app.command()` on `def hello(name: str):` creates a `hello` command.
- **Option** — A command-line flag or argument defined via type hints. Example: `name: str` becomes a positional argument, `--name str` becomes an option.
- **Argument** — A value passed on the command line. Positional arguments are required unless they have a default. Example: `user add Alice` where `Alice` is an argument.
- **`--help`** — Automatically generated documentation for each command, showing all options and their types.
- **Completion** — Shell tab-completion scripts that Typer generates. Users can hit tab to autocomplete commands and options.

## A tiny example

```python
# typer_demo.py
from typer import Typer

app = Typer()

@app.command()
def hello(name: str, excited: bool = False):
    """Say hello to someone."""
    greeting = f"Hello, {name}!"
    if excited:
        greeting += " 🎉"
    print(greeting)

if __name__ == "__main__":
    app()
```

Run `python typer_demo.py Alice --excited` and it prints `Hello, Alice! 🎉`. Run `python typer_demo.py --help` and Typer shows the automatically-generated help for the `hello` command.

## What I'll cover next

I want to install Typer with uv and build a minimal CLI app that uses both positional and optional arguments. Then I'll follow the official quickstart to see what trips me up and write that up in notes.