import typer

app = typer.Typer()


@app.command()
def greet(
    name: str = typer.Argument(help="The person to greet"),
    count: int = typer.Option(1, "--count", help="Number of times to greet"),
    loud: bool = typer.Option(False, "--loud", help="Uppercase the greeting"),
):
    """Greet NAME a given number of times."""
    msg = f"Hello {name}!"
    if loud:
        msg = msg.upper()
    for _ in range(count):
        typer.echo(msg)


if __name__ == "__main__":
    app()
