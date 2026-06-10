# Installed Typer and ran my first CLI hello-world

I wanted to try making a CLI app with Typer. Heard it's built on Click but uses type hints instead of decorator boilerplate.

## Install

Used uv since the rest of the kit runs on it:

```
uv pip install typer
```

Installed fast — no dependencies pulled in beyond what I already had. Version 0.15.x.

## First hello-world

Created `hello.py`:

```python
import typer

app = typer.Typer()


@app.command()
def greet(name: str):
    print(f"Hello {name}!")


if __name__ == "__main__":
    app()
```

Ran it:

```
python hello.py greet World
```

Output: `Hello World!`

## What I noticed

- The `@app.command()` decorator auto-detects the function signature and maps it to CLI args.
- `typer.run()` is the simpler alternative for single-command scripts — I could have used `typer.run(greet)` instead of the app pattern.
- The `--help` output is generated automatically: `python hello.py --help` lists all commands.

## What tripped me up

- I forgot the `if __name__ == "__main__": app()` at first. Without it, nothing happens when running the script.
- Typer expects `name: str` as a positional argument by default. I had to explicitly add `typer.Argument()` to customize it. For optional flags I'd use `typer.Option()`.

## Next

I want to try adding `typer.Option()` for flag-style arguments, and maybe a subcommand structure with multiple commands.
