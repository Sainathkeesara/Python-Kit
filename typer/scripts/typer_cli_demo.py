# typer_cli_demo.py — Minimal CLI app with positional and optional arguments
# Install with: uv run --with typer typer_cli_demo.py <arg> [--option VALUE]

from typer import Typer

app = Typer(help="A minimal CLI demo using Typer")

@app.command()
def greet(
    name: str,            # positional argument
    count: int = 1,       # optional argument with default
    loud: bool = False    # boolean flag
):
    """Greet someone multiple times, optionally loudly."""
    message = f"Hello, {name}!"
    if loud:
        message = message.upper()
    for _ in range(count):
        print(message)

if __name__ == "__main__":
    app()