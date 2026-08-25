# last_verified: 2026-08-25 · typer n/a
# Companion script for typer/notes/2026-06-10-first-typer-hello-world.md

import typer

app = typer.Typer()


@app.command()
def greet(name: str):
    print(f"Hello {name}!")


if __name__ == "__main__":
    app()
