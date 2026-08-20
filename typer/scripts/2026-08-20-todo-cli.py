# last_verified: 2026-08-20 · typer 0.27.1
# A first Typer() app with subcommands — add / list / done.
# The quickstart only showed single commands, so this is me pushing
# past that into a small todo list that actually persists.

import json
from pathlib import Path

import typer

app = typer.Typer(help="A tiny todo list you control from the terminal.")

# Stored next to wherever you run it, so the data survives between runs.
DATA = Path("todos.json")


def load_todos():
    # No file on the first run — that's fine, start empty.
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text())


def save_todos(todos):
    DATA.write_text(json.dumps(todos, indent=2))


def next_id(todos):
    # ids only ever grow, so "done 2" still means the same todo after a week.
    return max((t["id"] for t in todos), default=0) + 1


@app.command()
def add(task: str):
    """Add a task to the list."""
    todos = load_todos()
    new_id = next_id(todos)
    todos.append({"id": new_id, "task": task, "done": False})
    save_todos(todos)
    typer.echo(f"added #{new_id}: {task}")


@app.command("list")
def list_todos(show_done: bool = False):
    """Show open tasks (include finished ones with --show-done)."""
    todos = load_todos()
    for todo in todos:
        if todo["done"] and not show_done:
            continue
        mark = "x" if todo["done"] else " "
        typer.echo(f"[{mark}] #{todo['id']} {todo['task']}")


@app.command()
def done(task_id: int):
    """Mark a task as finished by its id."""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == task_id:
            todo["done"] = True
            save_todos(todos)
            typer.echo(f"done #{task_id}: {todo['task']}")
            return
    # Unknown id is the same "wrong input" shape as a missing file — say so.
    typer.echo(f"no task with id {task_id}", err=True)


if __name__ == "__main__":
    app()
