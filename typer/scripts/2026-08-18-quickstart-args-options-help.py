# last_verified: 2026-08-18 · typer n/a
# Following the official typer quickstart: single command, positional argument,
# optional argument with default, and a flag. --help is generated for free.

import typer


def main(
    name: str,                 # positional argument -- required
    lastname: str = "",        # optional argument, default ""
    formal: bool = False,      # --formal / --no-formal flag
):
    """Print a greeting, the way the quickstart does it."""
    if formal:
        typer.echo(f"Good day, {name} {lastname}.".strip())
    else:
        typer.echo(f"Hey {name} {lastname}!".strip())


if __name__ == "__main__":
    typer.run(main)