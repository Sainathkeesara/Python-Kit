# last_verified: 2026-08-26 · typer 0.15.x

import typer

app = typer.Typer()


@app.command()
def greet(name: str):
    print(f"Hello {name}!")


if __name__ == "__main__":
    app()