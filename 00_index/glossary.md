# Glossary

## httpie
- **HTTPie** — A user-friendly CLI HTTP client for the API age, built for testing and interacting with REST APIs.

## mypy
- **Static type checker** — A tool that analyzes code without running it, checking that type annotations are consistent with actual usage.
- **Type annotation** — A hint you add to Python code telling mypy what type a variable should be (e.g. `def greet(name: str) -> str:`).
- **Gradual typing** — mypy's ability to check partially-typed code; unannotated functions are assumed to return `Any`.
- **`Any`** — The dynamic type that disables type-checking on any expression; the escape hatch from strict checking.
- **`reveal_type()`** — A debug function that prints the inferred type of any expression; not available at runtime.
- **`# type: ignore`** — A comment telling mypy to skip type-checking a specific line.
- **`--strict`** — A flag enabling strict options: checking untyped defs, disallowing `Any`, requiring return types.
- **Stub file (`.pyi`)** — A file declaring type signatures without implementation, used for third-party packages.
- **strict mode** — A mypy configuration that enables the strictest set of type-checking rules.
- **incremental mode** — mypy's ability to cache previous results and only re-check changed files.

## pip-audit
- **CVE** — A publicly disclosed security vulnerability with an ID like `CVE-2023-12345`.
- **OSV** — Open Source Vulnerabilities database that pip-audit queries under the hood.
- **PYSEC** — PyPI-specific advisory ID format (e.g. `PYSEC-2023-100`).
- **`--fix`** — Experimental flag that attempts to auto-upgrade vulnerable packages.

## pipdeptree
- **Top-level package** — A package installed directly by the user (e.g. `pip install requests`).
- **Transitive dependency** — A dependency of a direct dependency (indirect dependency).
- **Dependency conflict** — When two packages require incompatible versions of the same third package.
- **`--json`** — Output the dependency tree as JSON instead of the default text tree.
- **`--warn silence`** — Suppress CVE advisory warnings so the output can be read cleanly.
- **`--freeze`** — Output packages as `pkg==version` lines, suitable for piping into grep.

## pre-commit
- **Hook** — A script or command that runs before a commit is finalized, defined in `.pre-commit-config.yaml`.
- **Repo** — In pre-commit, a source repository that provides hooks (e.g. `https://github.com/pre-commit/pre-commit-hooks`).
- **rev** — The tag or commit to pin a pre-commit hook source to.
- **ID** — The identifier of a specific hook within a pre-commit source repo.

## py (Ruff)
- **Linter** — Ruff's lint rules that detect code issues; configured under `[tool.ruff.lint]`.
- **Formatter** — Ruff's code formatter that rewrites files to a consistent style; configured under `[tool.ruff.format]`.
- **AST (Abstract Syntax Tree)** — The tree representation of source code that Ruff parses to apply lint and format rules.
- **lint** — The process of statically analyzing code to catch errors, bugs, and style issues.

## py-spy
- **Sampling profiler** — A profiler that periodically inspects the call stack of a running Python process.
- **flamegraph** — A visualization of program execution showing which functions consume the most CPU time.
- **record** — A py-spy subcommand that captures a profiling dump to disk.
- **top** — A py-spy subcommand that displays a live, top-like view of hot functions.
- **CPU-bound** — Code that spends most of its time using the CPU rather than waiting for I/O.
- **speedscope** — A web-based viewer for flamechart/flamegraph data; py-spy can export JSON in speedscope format.

## pyproject.toml
- **pyproject.toml** — The Python project configuration file (PEP 518 / PEP 621), used to declare build system, project metadata, and tool settings.
- **`[build-system]`** — Section declaring the build backend (e.g. setuptools, hatchling) and its requirements.
- **`[project]`** — Section for project metadata (name, version, dependencies, Python version requirement).
- **PEP 517** — The specification for a build-system independent format for source trees; defines how backends like hatchling are invoked.
- **PEP 621** — The specification for storing project metadata (name, version, dependencies) in the `[project]` table of `pyproject.toml`.

## pytest
- **assert** — Python's built-in assertion statement; pytest rewrites it to provide detailed failure messages.
- **fixture** — A pytest function that provides setup/teardown or test data, injected into test functions by parameter name.
- **parametrize** — A pytest decorator (`@pytest.mark.parametrize`) that runs a test function against multiple sets of arguments.
- **test discovery** — pytest's automatic collection of test functions (files matching `test_*.py`, functions named `test_*`).
- **xunit-style setup** — Module/class-level `setup_method` / `teardown_method` functions, inherited from the xUnit tradition.

## ruff
- **Rule selection** — Choosing which lint rules Ruff applies; controlled by the `select` setting.
- **per-file-ignores** — A Ruff configuration that disables specific rules for specific files or directories.
- **target-version** — The minimum Python version Ruff should target when formatting or linting.

## tox
- **env list** — The set of test environments defined in `tox.ini` and shown with `tox -l`.
- **-e flag** — The tox flag that selects which environment(s) to run (e.g. `tox -e py311`).
- **passing args through** — Using `--` to forward arguments from tox into the underlying test runner (e.g. `tox -e py311 -- -k test_name`).

## ty
- **Type inference** — Ty figuring out types even when annotations are not written (e.g. `x = 42` implies `int`).
- **PEP 484** — The Python specification that defines type annotation syntax (`Optional[str]`, `List[int]`, `Union[str, int]`, etc.).

## typer
- **Command** — A function decorated with `@app.command()` that becomes a CLI subcommand.
- **Option** — A command-line flag defined via type hints (e.g. `--name` becomes an option, `name` becomes a positional argument).
- **Argument** — A value passed positionally on the command line; required unless it has a default.
- **`--help`** — Automatically generated documentation for each command, showing all options and their types.
- **Completion** — Shell tab-completion scripts that Typer generates for bash, zsh, and fish.

## uv
- **uv** — A fast Python package and project manager (by Astral).
- **Virtual environment** — An isolated Python environment; uv can create and manage these without a separate `virtualenv` tool.
- **`uv sync`** — Command that synchronises the project environment with the lock file.
- **`uv add`** — Command that adds a dependency to `pyproject.toml` and updates the lock file.
- **`uv lock`** — Command that generates or updates the lock file without installing packages.
- **`uv run`** — Command that runs a script or command in the project's virtual environment.
- **`uv tool`** — Command for managing globally installed tools (equivalent to `pipx`).
- **`uv pip`** — Pip-compatible interface for users migrating from pip.
- **`uv python`** — Command for managing Python versions.
- **dev-dependencies** — Dependencies marked for development only; they are installed but not included in the published package metadata.
- **scaffold** — A project skeleton created by `uv init` with default directories and a `pyproject.toml`.
- **PEP 723** — Python Enhancement Proposal that allows inline script metadata/declarations in a special comment block.
- **ephemeral venv** — A temporary virtual environment created on-the-fly for a single run.

## uv.lock
- **Lockfile** — A file that pins exact versions of every direct and transitive dependency, ensuring reproducible installs.
- **Resolution** — The process of selecting compatible versions of all dependencies that satisfy the project's requirements.
- **Transitive dependency** — A dependency of a direct dependency (indirect dependency).
- **`[[package]]` section** — TOML array entry in `uv.lock` describing a single resolved package.
- **`[metadata]` section** — The top-level metadata block in `uv.lock` containing the resolver version and install strategy.
- **Hashes** — Cryptographic checksums (SHA256, SHA512) stored in `uv.lock` for each package to verify integrity across installs.

## rich
- **Console** — The main Rich object (`from rich.console import Console`); everything flows through it.
- **Renderable** — Anything Rich knows how to display: a `Table`, a `Panel`, a `Text` object, or a string.
- **Panel** — A bordered box drawn around content.
- **Table** — A component for structured column/row display with alignment, styles, and headers.
- **Live** — A context manager that re-renders output in place, used for progress and real-time dashboards.
- **Progress** — A pre-built progress bar widget supporting multiple bars, transfer speeds, and spinners.
- **Markdown** — Renders markdown text to formatted terminal output.
- **Syntax** — Syntax-highlights source code with a Pygments-based theme.
