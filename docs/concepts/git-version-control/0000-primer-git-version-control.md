# Git Version Control — quick primer

> First-day notes on Git version control. What it is, why it matters, and the key ideas to know.

## What is it?

Git is a distributed version control system — it tracks changes to files over time so you can go back to any previous state, see who changed what, and collaborate with others without stepping on each other's work. I've been using it for a while and it's one of those tools I can't imagine working without.

Think of it like a save-game system for your code. Every time you "commit" (save a checkpoint), Git records a snapshot of every file. You can later jump to any commit, compare changes between them, or merge different lines of work together.

## Why does it matter for Python?

As a Python developer, nearly everything I do involves version control. The projects I work on — whether they're scripts, libraries, or full applications — all live in Git repositories. Beyond just saving work, Git enables:
- Experimenting with new features in branches without breaking the main codebase.
- Collaborating with other developers through pull requests and code review.
- Automating quality checks with pre-commit hooks (which run linters and type checkers before each commit).
- Reproducing any past state of the project when debugging issues.

In the Python-Kit specifically, tools like pre-commit integrate directly with Git — they install hooks that run automatically when I run `git commit`, checking my code with Ruff, mypy, or pytest before the commit goes through.

## Key terminology

- **Repository (repo)** — A directory managed by Git, containing all files and their entire history. Example: the `/work/Python-Kit` directory is a Git repo.
- **Commit** — A snapshot of all tracked files at a point in time, with a message describing what changed. Example: `git commit -m "fix: handle empty input in parser"`.
- **Branch** — A separate line of development. The default branch is usually `main` or `master`. Example: `git checkout -b fix-login-bug` creates a new branch to work on a bug fix.
- **Stage (index)** — The set of changes you've marked to include in the next commit. Example: `git add src/parser.py` stages that file for the next commit.
- **Remote** — A copy of the repository hosted somewhere else, like GitHub. Example: `git push origin main` sends commits to the remote named `origin`.
- **Pull request (PR)** — A proposal to merge changes from one branch into another, typically reviewed by another developer before merging.
- **`HEAD`** — A pointer to the most recent commit on the current branch. If I'm on `main`, `HEAD` points to the latest commit on `main`.
- **`.gitignore`** — A file that tells Git which files or patterns to ignore (like `__pycache__/`, `.env`, or `*.pyc`).

## A concrete example

Here's the basic workflow I use every day:

```bash
# Start working on a new feature
git checkout -b add-validation

# Make changes, then stage and commit them
git add src/validator.py
git commit -m "feat: add input validation function"

# Push to GitHub and open a pull request
git push origin add-validation
# Then open a PR on GitHub comparing add-validation → main
```

After the PR is reviewed and merged, I switch back to main and pull the latest changes:

```bash
git checkout main
git pull origin main
```

## How this connects to what's next

Git is the foundation that tools like pre-commit and GitHub Actions build on. Once I understand commits, branches, and remotes, I can set up pre-commit hooks that automatically lint my code before every commit, and configure CI pipelines that run tests on every push.
