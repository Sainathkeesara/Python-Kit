# Ruff — quick primer

> First-day notes for someone who's never used Ruff. Personal voice, plain language.

## What is it?
Ruff is an extremely fast Python linter and code formatter written in Rust. It aims to replace multiple Python quality tools like Flake8, Black, isort, and others while being 10-100x faster. Ruff sits in the Python developer tooling space, providing both linting (finding issues) and formatting (fixing code style) capabilities in a single package.

## What does it do?
Ruff lints Python code for errors, style issues, and potential bugs using over 900 built-in rules. It can automatically fix many of these issues. Ruff also formats code to enforce consistent style, similar to Black. It works with pyproject.toml for configuration and includes caching to avoid re-analyzing unchanged files.

## Why does it exist?
Before Ruff, Python developers had to use multiple separate tools: Flake8 for linting, Black for formatting, isort for import sorting, etc. Running these tools individually was slow, especially on large codebases. Ruff was created to provide all these functionalities in a single, extremely fast tool, dramatically improving developer experience during local development and CI processes.

## Key terminology
- **Linter** — A tool that analyzes code for potential errors and style issues. Example: Ruff flags unused variables in your Python file.
- **Formatter** — A tool that automatically reformats code to follow style guidelines. Example: Ruff reformats your code to have consistent line lengths and indentation.
- **Rule** — A specific check that Ruff performs on your code. Example: Rule F401 warns about imported modules that are unused.
- **Fix** — Automatic correction that Ruff can apply to resolve certain issues. Example: Ruff can automatically remove unused imports when it finds them.
- **Cache** — Storage of previous analysis results to speed up subsequent runs. Example: Ruff remembers which files it has already checked and skips them if unchanged.
- **pyproject.toml** — Configuration file where you can customize Ruff's behavior. Example: You can enable/disable specific rules in this file.
- **Member access** — Ruff feature that allows accessing attributes without triggering certain false positives. Example: Using ruff: noqa comments to suppress specific warnings.

## A tiny example
```bash
# Install Ruff
pip install ruff

# Create a Python file with issues
echo 'import os  # unused import
x=1+2  # missing spaces
print("hello")' > example.py

# Check the file with Ruff
ruff check example.py

# Fix issues automatically
ruff fix example.py

# Format the file
ruff format example.py
```
This example shows installing Ruff, creating a file with common issues, checking for problems, automatically fixing them, and then formatting the code.

## What I'll cover next
I plan to explore configuring Ruff with pyproject.toml, integrating it into development workflows, and learning how to create custom rules or presets for specific project needs.