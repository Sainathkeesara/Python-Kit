# Generated my first uv.lock

I already had uv installed from earlier. Ran `uv init --app demo-lock` and `cd demo-lock`, then `uv add requests`. That created a `uv.lock` file beside the `pyproject.toml`.

## What's inside

It's a TOML file. Top line is `version = 1`. Then a big `[[package]]` list. Each package has:

- `name` — the package name
- `version` — exact pinned version
- `source` — where it came from (PyPI, with `url` and `verify_checksum`)
- `dependencies` — other packages it needs, with version constraints
- `sdist` and `wheel` — hashes for integrity checking

I was surprised how many transitive deps `requests` pulled in — about 6 packages in the lockfile for just one direct dependency.

## What tripped me up

I tried `cat uv.lock` first and the file is pretty long. `head -40 uv.lock` was better for a quick look. The `[[package]]` sections are grouped alphabetically, not by dependency order.
