"""tried-typer-calculator.py — building a CLI calculator with Typer"""

import typer

app = typer.Typer()

# Typer turns function docstrings into --help text automatically
# I used typer.Argument() for the add command to see how it compares to
# just declaring positional params (like sub, mul, div below)


@app.command()
def add(
    a: float = typer.Argument(help="First number"),
    b: float = typer.Argument(help="Second number"),
):
    """Add two numbers together"""
    typer.echo(f"{a} + {b} = {a + b}")


@app.command()
def sub(a: float, b: float):
    """Subtract b from a"""
    typer.echo(f"{a} - {b} = {a - b}")


@app.command()
def mul(a: float, b: float):
    """Multiply two numbers"""
    typer.echo(f"{a} * {b} = {a * b}")


@app.command()
def div(a: float, b: float):
    """Divide a by b"""
    if b == 0:
        # Typer.Exit(1) exits cleanly without a traceback
        typer.echo("Error: cannot divide by zero", err=True)
        raise typer.Exit(1)
    typer.echo(f"{a} / {b} = {a / b}")


if __name__ == "__main__":
    app()
