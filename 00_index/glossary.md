# Glossary

## Concepts

### Git
- **Repository (repo)** — A directory managed by Git, containing all files and their entire history.
- **Commit** — A snapshot of all tracked files at a point in time, with a message describing what changed.
- **Branch** — A separate line of development. The default branch is usually `main` or `master`.
- **Stage (index)** — The set of changes you've marked to include in the next commit.
- **Remote** — A copy of the repository hosted somewhere else, like GitHub.
- **Pull request (PR)** — A proposal to merge changes from one branch into another, reviewed before merging.
- **`HEAD`** — A pointer to the most recent commit on the current branch.
- **`.gitignore`** — A file that tells Git which files or patterns to ignore.

### Python Programming Fundamentals
- **Variable** — A name that holds a value. Example: `timeout = 30`
- **String** — Text data wrapped in quotes. Example: `name = "pytest"`
- **List** — An ordered sequence, written with square brackets. Example: `tools = ["ruff", "mypy", "pytest"]`
- **Dictionary** — Key-value pairs, written with curly braces. Example: `settings = {"strict": True, "ignore": ["*.pyc"]}`
- **Function** — Reusable code defined with `def`, takes inputs and returns a result.
- **Loop** — Repeat code for each item using `for`.
- **Conditional** — Branch code based on a condition with `if`/`elif`/`else`.
- **Import** — Load code from another module.
- **Comprehension** — A compact expression that builds a list, dict, or set from an iterable in one line (e.g. `[x * 2 for x in items]`).
- **Generator** — A function using `yield` that produces values lazily, one at a time, without building the whole sequence in memory.
- **Exception** — An error raised at runtime that can be caught with `try`/`except` so the program can recover instead of crashing.
- **Dataclass** — A class decorated with `@dataclass` that automatically generates `__init__`, `__repr__`, and `__eq__` methods from type-annotated fields, reducing boilerplate for data-holding classes.
- **Context manager** — An object that implements `__enter__` and `__exit__` to set up and tear down a resource block, used with the `with` statement (e.g. `with open(...) as f:`).
- **Decorator** — A function that wraps another function or class to modify its behaviour without changing its source code, applied with the `@decorator` syntax above the definition.

### Python Packaging & Project Config
- **pyproject.toml** — The standard config file for Python projects, defined by PEP 518 and PEP 621.
- **PEP 621** — The standard that defines how to put project metadata directly in pyproject.toml under a `[project]` table.
- **Build backend** — The library that builds your package into a distribution (setuptools, hatchling, flit_core, pdm-backend).
- **Dependencies** — Other packages your project needs at runtime.
- **Lockfile** — A file that pins exact versions of every dependency and transitive dependency.
- **Virtual environment** — An isolated directory with its own Python interpreter and package set.
- **SDist (source distribution)** — A compressed archive of source code that can be built and installed.
- **Wheel** — A pre-built distribution format that installs faster than SDist.
- **Wheel manifest** — The list of files packaged inside a built wheel, inspectable with `unzip -l`. Build scripts use it to confirm exactly what ships in a distribution.
- **Entry point** — A function exposed as a CLI command via the `[project.scripts]` table.
- **tomllib** — Python's standard-library TOML parser (3.11+), used by scripts in this kit to read pyproject.toml programmatically.

### Software Testing Principles
- **Unit test** — Tests a single function or method in isolation.
- **Assertion** — A check that a condition is true; a test passes if all its assertions pass.
- **Test fixture** — Setup code that creates data or state before a test runs.
- **Parametrization** — Running the same test logic with different input values.
- **Test coverage** — A metric showing what percentage of code lines are executed during tests.
- **Red-Green-Refactor** — A TDD cycle: write a failing test (red), write code to make it pass (green), then clean up the code (refactor).
- **Mock** — A fake object that replaces a real dependency during testing.
- **Test double** — A generic term for any stand-in object (stub, fake, mock, spy) that replaces a real dependency during testing.
- **Boundary value** — A value at the edge of a valid input range (e.g. `12`, `13`, `20` around a `< 13` threshold), where off-by-one bugs tend to hide.
- **AAA pattern** — Arrange–Act–Assert: writing each test as setup (Arrange), calling the code under test (Act), and checking the result (Assert) so each beat is explicit and readable.
- **Regression** — A bug that reappears after a change.

### Static Type Checking & Type Hints
- **Type hint** — An annotation on a variable, parameter, or return value indicating its expected type.
- **Static type checker** — A tool that analyzes source code without running it to find type inconsistencies.
- **Gradual typing** — Python's approach where you can add type hints to part of your codebase while leaving the rest untyped.
- **`Any`** — A special type that tells the checker "this could be anything, don't check it."
- **`Optional[str]`** — Shorthand for `Union[str, None]`. Means the value could be a string or `None`.
- **Type stub (`.pyi`)** — A file that declares types for code you didn't write, like third-party libraries without built-in type hints.
- **`reveal_type()`** — A debugging function that makes the type checker print what type it infers for an expression.
- **`--strict`** — A mode that enables all the strictest checks in a type checker.
- **`Protocol`** — A class from `typing` that declares structural subtyping: any object whose methods match the declared shape satisfies the protocol, with no shared base class required.
- **`TypedDict`** — A type that gives a plain dictionary a fixed set of keys with known value types, so the checker can validate dict shapes.
- **TypeVar / generics** — A type variable (`T = TypeVar("T")`) that lets a function or class preserve the element type of its inputs, e.g. a helper returning `list[T]` keeps the concrete type of the list passed in.

### Virtual Environment & Dependency Mgmt
- **Virtual environment** — An isolated Python environment with its own packages.
- **`pyproject.toml`** — The modern Python project config file where dependencies and build settings are declared.
- **`uv.lock`** — A lockfile generated by `uv` that records exact versions and hashes of every dependency.
- **Lockfile** — A file that pins every transitive dependency to a specific version and checksum.
- **Dependency resolution** — The process of finding a set of package versions that satisfy all version constraints across the dependency tree.
- **Transitive dependency** — A dependency of a direct dependency (indirect dependency).
- **Marker** — A condition that controls when a dependency is installed, based on Python version, OS, or platform.
- **`pip-audit`** — A tool that scans installed packages against known vulnerability databases and reports CVEs.
- **src layout** — A project structure where source code lives in a `src/` directory, so tests import the installed package rather than the working directory.
- **flat layout** — A project structure where source code lives at the repository root, which can mask packaging bugs because tests resolve imports from `.` instead of the installed artifact.

### Security Best Practices
- **Dependency scanning** — Checking installed packages against known vulnerabilities, typically with `pip-audit` or similar tools.
- **Secrets management** — Keeping API keys, passwords, and tokens out of source code by using environment variables, vaults, or secret managers.
- **Input validation** — Verifying that data from users, files, or the network matches expected types and ranges before processing it.
- **Least privilege** — Giving code only the permissions it needs to do its job, rather than broad access like an admin account.
- **Static analysis** — Tools that scan code without running it to find security anti-patterns (e.g. `bandit` catching `eval()` or hardcoded secrets).
- **SBOM (Software Bill of Materials)** — A machine-readable list of every component in a project, useful for tracking which vulnerabilities affect it.

## httpie
- **HTTPie** — A user-friendly CLI HTTP client for the API age, built for testing and interacting with REST APIs.
- **`--ignore-stdin`** — A flag that stops HTTPie from reading a request body from stdin, so requests don't hang when stdin is closed or redirected (cron, CI runners).
- **`--check-status`** — A flag that turns non-2xx responses into a non-zero exit code (3 on 3xx, 4 on 4xx, 5 on 5xx), so a bad response fails a script instead of printing a body and passing.
- **Request-item DSL** — The `key=value` pairs that follow the URL in an httpie command. They become form fields or JSON body entries depending on the content-type header.
- **`--offline`** — Builds the full request and prints it without sending anything, implicitly activating `--print=HB` so headers and body are visible.
- **Session reuse** — Persisting cookies and auth headers in a session file so subsequent calls inherit them, avoiding repeated authentication.
- **Session auth** — Using `http --session=<path>` to store and reuse cookies and auth headers across multiple requests to the same host.
- **Inline auth** — Passing credentials directly on the command line for each request instead of relying on a persisted session.

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
- **Vulnerability** — A known security flaw in a specific package version. Advisory databases assign identifiers like PYSEC, CVE, or GHSA.
- **Advisory** — The published record of a vulnerability, usually with a recommended fixed version. pip-audit reports advisories and suggests upgrading to a patched version.
- **`--fix`** — Experimental flag that attempts to auto-upgrade vulnerable packages.
- **`--ignore-vuln <id>`** — Skips a specific advisory by identifier. Use this to silence a known false-positive for one package.
- **`--locked`** — Audits a `pyproject.toml` or lockfile directly without needing a live environment. Added in pip-audit 2.7.

## pipdeptree
- **Top-level package** — A package installed directly by the user (e.g. `pip install requests`).
- **Transitive dependency** — A dependency of a direct dependency (indirect dependency).
- **Dependency conflict** — When two packages require incompatible versions of the same third package.
- **Cycle detection** — Identifying circular dependencies where package A depends on B and B depends on A, which can break installs.
- **Leaf package** — A package with no outgoing dependencies of its own; in a dependency tree it sits at the leaves.
- **Reverse-dependency count** — How many installed packages depend on a given package, used to gauge a package's blast radius before changing or removing it.
- **Dependency-health report** — A summary combining `pipdeptree --warn`, `--reverse`, and `--json` into one pass: conflicts, top-level and leaf counts, and the most-depended-on packages.
- **`--json`** — Output the dependency tree as JSON instead of the default text tree.
- **`--warn silence`** — Suppress CVE advisory warnings so the output can be read cleanly.
- **`--freeze`** — Output packages as `pkg==version` lines, suitable for piping into grep.

## pre-commit
- **Hook** — A script or command that runs before a commit is finalized, defined in `.pre-commit-config.yaml`.
- **Repo** — In pre-commit, a source repository that provides hooks (e.g. `https://github.com/pre-commit/pre-commit-hooks`).
- **rev** — The tag or commit to pin a pre-commit hook source to.
- **ID** — The identifier of a specific hook within a pre-commit source repo.
- **`--all-files`** — A pre-commit flag that runs hooks on every tracked file, not just staged changes.
- **`SKIP=`** — An environment variable that skips specific hooks by ID for a single commit (e.g. `SKIP=ruff git commit`).
- **CI parity check** — Running pre-commit `--all-files` locally to confirm the same hooks will pass in CI, where `SKIP` bypasses are not available.

## prc
- **pre-commit** — A framework for managing and running git hooks; `prc` is the short alias used for first-contact notes and configs in this kit.
- **CI parity** — The guarantee that a local `pre-commit run --all-files` result matches what CI will see, since CI cannot honour `SKIP=` bypasses.

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
- **dump** — A py-spy subcommand that prints the current call stack of every thread to the terminal and exits immediately, with no sampling window and no output file.
- **CPU-bound** — Code that spends most of its time using the CPU rather than waiting for I/O.
- **speedscope** — A web-based viewer for flamechart/flamegraph data; py-spy can export JSON in speedscope format.

## pyproject.toml
- **pyproject.toml** — The Python project configuration file (PEP 518 / PEP 621), used to declare build system, project metadata, and tool settings.
- **`[build-system]`** — Section declaring the build backend (e.g. setuptools, hatchling) and its requirements.
- **`[project]`** — Section for project metadata (name, version, dependencies, Python version requirement).
- **PEP 517** — The specification for a build-system independent format for source trees; defines how backends like hatchling are invoked.
- **PEP 621** — The specification for storing project metadata (name, version, dependencies) in the `[project]` table of `pyproject.toml`.
- **tomllib** — Python's built-in TOML parser (3.11+) used for validating pyproject.toml structure programmatically.

## pytest
- **assert** — Python's built-in assertion statement; pytest rewrites it to provide detailed failure messages.
- **fixture** — A pytest function that provides setup/teardown or test data, injected into test functions by parameter name.
- **parametrize** — A pytest decorator (`@pytest.mark.parametrize`) that runs a test function against multiple sets of arguments.
- **test discovery** — pytest's automatic collection of test functions (files matching `test_*.py`, functions named `test_*`).
- **xunit-style setup** — Module/class-level `setup_method` / `teardown_method` functions, inherited from the xUnit tradition.
- **conftest.py** — A special file pytest uses for sharing fixtures, hooks, and configuration across test directories.
- **scoping** — Controls how often a fixture runs (e.g. `session`, `module`, `class`, `function`) to balance setup cost against test isolation.
- **`tmp_path`** — pytest's built-in fixture providing a temporary directory unique to each test function; files created inside it are removed automatically.
- **`tmp_path_factory`** — pytest's session-scoped fixture for creating temporary directories shared across an entire test session, useful for expensive one-time setup.

## pyright
- **Pyright** — A fast static type checker for Python, written in TypeScript and used as the engine behind Pylance in VS Code.
- **`pyrightconfig.json`** — Project-level config file controlling Python version, include/exclude paths, and strictness (`"off"`, `"basic"`, `"strict"`).
- **Diagnostics** — Errors and warnings Pyright reports, each with a file, line, column, and message.
- **Type stubs (`.pyi`)** — Skeleton files declaring types for third-party libraries that don't ship their own annotations; Pyright auto-downloads these for popular packages.
- **`reportMissingImports`** — Setting to control whether unresolved imports produce warnings or are silenced.
- **`typeCheckingMode`** — `"off"`, `"basic"`, or `"strict"`; strict enables every diagnostic.
- **Pylance** — The VS Code extension wrapping Pyright, providing type checking, autocomplete, and go-to-definition in the editor.

## ruff
- **Rule selection** — Choosing which lint rules Ruff applies; controlled by the `select` setting.
- **per-file-ignores** — A Ruff configuration that disables specific rules for specific files or directories.
- **`extend-safe`** — A Ruff lint configuration that restricts `--fix` to safe auto-fixes only, avoiding changes that could break code.
- **`--unsafe-fixes`** — A Ruff CLI flag that overrides `extend-safe` and allows potentially unsafe auto-fixes to be applied.
- **target-version** — The minimum Python version Ruff should target when formatting or linting.

## tox
- **env list** — The set of test environments defined in `tox.ini` and shown with `tox -l`.
- **-e flag** — The tox flag that selects which environment(s) to run (e.g. `tox -e py311`).
- **passing args through** — Using `--` to forward arguments from tox into the underlying test runner (e.g. `tox -e py311 -- -k test_name`).

## ty
- **Type inference** — Ty figuring out types even when annotations are not written (e.g. `x = 42` implies `int`).
- **PEP 484** — The Python specification that defines type annotation syntax (`Optional[str]`, `List[int]`, `Union[str, int]`, etc.).
- **strict mode** — A Ty configuration that enforces checking all functions, even ones without annotations; similar to mypy's `--strict`.
- **Unannotated** — A function or variable with no type hint; in Ty's strict mode, these are flagged as errors.
- **zero-config** — Ty's philosophy of working out of the box with no manual configuration needed.

## typer
- **Command** — A function decorated with `@app.command()` that becomes a CLI subcommand.
- **Option** — A command-line flag defined via type hints (e.g. `--name` becomes an option, `name` becomes a positional argument).
- **Argument** — A value passed positionally on the command line; required unless it has a default.
- **Required positional argument** — A bare-typed parameter without a default (e.g. `name: str`); Typer makes it positional and required, not an option.
- **`--no-` flag pair** — A parameter typed `bool` with a default (e.g. `formal: bool = False`) produces both `--formal` and `--no-formal` variants automatically.
- **Docstring-as-help** — Typer uses the command function's docstring as its `--help` text at no extra cost.
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
- **`[dependency-groups]`** — A pyproject.toml table for dev-only dependencies (e.g. `dev = ["ruff>=0.5", ...]`); `uv sync` installs them but they never appear in published metadata or the runtime dependency set.
- **uv_build** — A build backend that builds a src-layout package straight from a static pyproject.toml, with no setup.py; the backend uv recommends for new projects.
- **PEP 723** — Python Enhancement Proposal that allows inline script metadata/declarations in a special comment block.
- **ephemeral venv** — A temporary virtual environment created on-the-fly for a single run.
- **`uv lock --frozen`** — Validates the lock file against pyproject.toml without modifying it; fails if they're out of sync.
- **`uv export`** — Generates a requirements.txt or similar format from the project's dependencies for tools that don't use uv.lock.
- **`uvx`** — A command alias for `uv tool run` that executes a tool in an ephemeral environment without installing it globally.

## uv.lock
- **Lockfile** — A file that pins exact versions of every direct and transitive dependency, ensuring reproducible installs.
- **Resolution** — The process of selecting compatible versions of all dependencies that satisfy the project's requirements.
- **Transitive dependency** — A dependency of a direct dependency (indirect dependency).
- **`[[package]]` section** — TOML array entry in `uv.lock` describing a single resolved package.
- **`[metadata]` section** — The top-level metadata block in `uv.lock` containing the resolver version and install strategy.
- **Hashes** — Cryptographic checksums (SHA256, SHA512) stored in `uv.lock` for each package to verify integrity across installs.
- **source** — The origin of a resolved package in `uv.lock`: PyPI, a git URL, a local path, or a custom index.

## uvl
- **Dependency group** — A category of dependencies in `uv.lock` (e.g. `default`, `dev`) that controls which packages are installed together.
- **`--no-dev`** — A `uv sync` flag that skips packages in the `dev` dependency group.
- **uv.lock** — A lockfile generated by `uv` — the fast Python package manager. If you know `package-lock.json` from npm or `Cargo.lock` from Rust, you already understand the concept: it pins every single dependency (and sub-dependency) to exact versions so that everyone installing the project gets the same environment. uv writes it in a cross-platform TOML format.

## rich
- **Console** — The main Rich object (`from rich.console import Console`); everything flows through it.
- **Renderable** — Anything Rich knows how to display: a `Table`, a `Panel`, a `Text` object, or a string.
- **Panel** — A bordered box drawn around content.
- **Table** — A component for structured column/row display with alignment, styles, and headers.
- **Live** — A context manager that re-renders output in place, used for progress and real-time dashboards.
- **Progress** — A pre-built progress bar widget supporting multiple bars, transfer speeds, and spinners.
- **Markdown** — Renders markdown text to formatted terminal output.
- **Syntax** — Syntax-highlights source code with a Pygments-based theme.
- **Inspect** — Rich utility that dumps an object's attributes, methods, and source for quick debugging in the terminal.

## Git Version Control
- **Repository (repo)** — A directory managed by Git, containing all tracked files and their complete history.
- **Commit** — A snapshot of all tracked files at a point in time, paired with a message describing the change.
- **Branch** — A separate line of development, letting you work on features or fixes without affecting the main codebase.
- **Stage (index)** — The set of file changes you have marked for inclusion in the next commit using `git add`.
- **Working tree** — Files on disk that are not yet staged; the complement of the staging area.
- **Remote** — A hosted copy of the repository (e.g., on GitHub) that you can push to or pull from.
- **HEAD** — A pointer to the most recent commit on the currently checked-out branch.
- **Conventional Commits** — A convention for structuring commit messages with prefixes like `feat:`, `fix:`, `chore:`.
- **setuptools-scm** — A build-backend plugin that derives a package version from git tags instead of a hardcoded version file.
- **PEP 440** — The specification for Python version numbers and how they compare (e.g. `1.2.3` vs `1.2.4.dev0`), which version-from-tags output follows.
- **Tag** — A named, fixed reference to a specific commit, typically versioned like `v1.2.0`; used as the release point that dependents pin against.
- **Branch protection** — Repository rules that block direct pushes to a branch until required checks (e.g. a CI status check) pass.
- **CI gate** — A check that runs on every push and pull request, and must pass before a merge is allowed.

## Python Programming Fundamentals
- **Type hint** — An annotation on a variable, parameter, or return value indicating its expected type.
- **PEP 484** — The Python Enhancement Proposal that introduced standardised type hint syntax (`Optional[str]`, `List[int]`, `Union[str, int]`).
- **PEP 585** — The Python Enhancement Proposal that allows using built-in generics (`list[str]`, `dict[str, int]`) instead of `typing.List`, `typing.Dict`.
- **Marker** — A condition attached to a dependency that controls when it is installed (based on Python version, OS, or platform).

## Package & Dependency Management
- **Dependency resolution** — The process of selecting a set of package versions that satisfy all version constraints across the dependency tree.
- **requirements.txt** — A traditional pip dependency file listing packages line by line, often with version pins.
- **pip** — Python's standard package installer; retrieves packages from PyPI.
