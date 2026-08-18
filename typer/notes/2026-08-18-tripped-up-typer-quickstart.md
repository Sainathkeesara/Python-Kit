---
last_verified: 2026-08-18
tool_version: n/a
sources: []
---

# What tripped me up following the typer quickstart

I followed the official typer quickstart and mostly it just worked — which is the point of typer. The install was painless, the first example ran, and `--help` came along for free. But three things made me pause, and I want to remember them before I forget that they were ever confusing.

## 1. A plain `str` parameter is a required positional argument

The first example is just `def main(name: str)` and calling it gives you `argument name:... required`. I instinctively reached for `--name`, but typer makes bare-typed params positional by default. I got the flag I wanted only after I added a default: `name: str = ""` turns it into an optional option (`--name`). That's a neat trick but backwards from where my brain was coming from (argparse, where pretty much everything is an option unless you say otherwise).

## 2. `bool` defaults make flags, and `--no-` is free

`formal: bool = False` produced a `--formal` / `--no-formal` pair. I did not expect the `--no-formal` variant to exist without any extra code. It threw me for a second because I thought I'd get a single boolean flag and instead got two. Useful, but worth knowing before you design an API around one flag.

## 3. `--help` really is just there

I kept assuming I'd need to wire up help text. Nope — the docstring becomes the help. The smallest thing, and the biggest "oh" of the whole quickstart. I never wrote an argparse help string that fast in my life.

## What I'd try next

Now I want to move past the single-command example to the `Typer()` app with subcommands, and see how `typer.Argument(...)` / `typer.Option(...)` give finer control than bare type hints. The calculator and todo list scripts feel like the natural next step from here.

One more thing I noticed: the same file that was a one-command `typer.run()` script gets awkward fast once you have more than one of anything. The switch to a `Typer()` app instance with `@app.command()` decorations is the moment the quickstart really stopped being a toy for me.