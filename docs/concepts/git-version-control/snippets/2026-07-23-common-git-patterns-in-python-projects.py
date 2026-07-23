# last_verified: 2026-07-23 · Git Version Control n/a

import subprocess


def git(*args, cwd="."):
    """Run a git command and return stdout; raise on failure."""
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


# I check the working tree before staging anything.
status = git("status", "--porcelain")
if status:
    print("Uncommitted changes:\n", status)
else:
    print("Working tree clean — nothing to stage.")

# Create a feature branch off the current HEAD.
current = git("branch", "--show-current")
branch_name = f"feat/add-{current}"
branches = git("branch", "--list").splitlines()
if branch_name not in branches:
    git("checkout", "-b", branch_name)
    print(f"Created branch: {branch_name}")
else:
    print(f"Branch {branch_name} already exists.")

# List remote branches so I can see what collaborators are working on.
remotes = git("branch", "-r")
print("Remote branches:\n", remotes)
