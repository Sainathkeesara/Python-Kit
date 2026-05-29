# Typer quickstart notes

Tried the official Typer quickstart and here's what happened:

1. Installed Typer with `uv pip install typer`. No issues, installed quickly.

2. Created the first script with a simple command. It worked on the first try — the type hints for string and bool just worked without any extra config.

3. Adding the `--count` integer option required me to remember the syntax for optional arguments with defaults: `count: int = 1`. Without the default, Typer treats it as required.

4. The `--loud` flag was straightforward — just `loud: bool = False` and Typer automatically makes it optional. Passing `--loud` or `--no-loud` works as expected.

5. Running `python typer_cli_demo.py --help` shows the generated help, which is nice. It lists all arguments with their types.

6. Shell completion: the quickstart mentions it but I haven't tried it yet. That'll be for next time.