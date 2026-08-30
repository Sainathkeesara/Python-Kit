# last_verified: 2026-08-29 · typer
"""Minimal Typer CLI with subcommands, type-annotated params, and --help."""

import typer

app = typer.Typer(help="A tiny CLI with two subcommands.")
status_app = typer.Typer(help="Check status of things.")
app.add_typer(status_app, name="status")


@app.command()
def greet(name: str, loud: bool = False):
    """Greet someone by name."""
    msg = f"Hello, {name}"
    if loud:
        msg = msg.upper()
    typer.echo(msg)


@app.command()
def add(a: int, b: int):
    """Add two numbers."""
    typer.echo(f"{a} + {b} = {a + b}")


@status_app.command("server")
def status_server(host: str = "localhost", port: int = 8000):
    """Check if a server is reachable."""
    typer.echo(f"Checking {host}:{port}...")


@status_app.command("db")
def status_db(db_url: str):
    """Check database connectivity."""
    typer.echo(f"Connecting to {db_url}...")


if __name__ == "__main__":
    app()
