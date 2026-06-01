"""Minimal uv project with an external dependency.

I wanted to see how uv handles deps without a pyproject.toml.
PEP 723 inline metadata lets you declare them right in the script.
Run: uv run hello-with-dep.py
"""

# PEP 723 inline metadata — uv reads this block automatically
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///

import requests


def main() -> None:
    # Picked requests because it's simple — fetches JSON, no auth needed
    resp = requests.get("https://api.github.com")
    data = resp.json()

    print(f"GitHub API current_user_url: {data['current_user_url']}")
    print(f"Status code: {resp.status_code}")
    # uv created an ephemeral venv for requests automatically — no manual pip
    print("It works — uv installed requests into an ephemeral virtual env.")


if __name__ == "__main__":
    main()
