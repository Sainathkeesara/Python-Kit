# last_verified: 2026-07-23 · Git Version Control n/a

import subprocess
import tempfile
import os


def run(cmd, cwd=None):
    """Run a command and return stdout; raise if the command fails."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr.strip()}")
    return result.stdout.strip()


def main():
    # I'm using a temp directory so the script stays isolated from my real repos.
    with tempfile.TemporaryDirectory() as tmpdir:
        # Initialize a fresh repo.
        run(["git", "init"], cwd=tmpdir)
        run(["git", "config", "user.email", "learner@example.com"], cwd=tmpdir)
        run(["git", "config", "user.name", "Learner"], cwd=tmpdir)

        # Create an initial file and commit it.
        readme = os.path.join(tmpdir, "README.md")
        with open(readme, "w") as f:
            f.write("# Practice Repo\n")
        run(["git", "add", "README.md"], cwd=tmpdir)
        run(["git", "commit", "-m", "feat: initial readme"], cwd=tmpdir)

        # Create a feature branch off main.
        run(["git", "checkout", "-b", "feature-branch"], cwd=tmpdir)
        print("Branches:", run(["git", "branch"], cwd=tmpdir))
        print("Log:", run(["git", "log", "--oneline"], cwd=tmpdir))


if __name__ == "__main__":
    main()
