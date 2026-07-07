# last_verified: 2026-07-05 · Typer n/a
import typer

app = typer.Typer()

@app.command()
def greet(name: str, shout: bool = typer.Option(False, "--shout")):
    msg = f"Hello {name}"
    print(msg.upper() if shout else msg)

@app.command()
def bye(name: str):
    print(f"Goodbye {name}")

if __name__ == "__main__":
    app()
