"""Read a uv.lock file and list all locked package names."""

import tomllib

with open("uv.lock", "rb") as f:
    data = tomllib.load(f)

for pkg in data.get("package", []):
    print(pkg["name"])
