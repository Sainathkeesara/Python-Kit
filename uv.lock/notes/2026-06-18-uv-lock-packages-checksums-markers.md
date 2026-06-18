# Explored uv.lock: packages, checksums, markers

I already knew uv.lock was a lockfile. Today I dug into the specifics: what the version pins look like, where checksums live, and how markers work.

## Package entries

Each `[[package]]` in the TOML has `name`, `version`, and `source`. The version is the exact resolved version. Source tells where it came from:

```toml
[[package]]
name = "requests"
version = "2.32.3"
source = { registry = "https://pypi.org/simple" }
```

Transitive deps get the same treatment — every package in the tree is listed.

## Checksums

Each package has a `wheels` list with file hashes:

```toml
wheels = [
    { url = "https://files.pythonhosted.org/...", hash = "sha256:abc123..." },
]
```

And an `sdist` with its own hash. I noticed:
- Multiple wheels per package (different Python versions, platforms)
- Each hash is prefixed with the algorithm (`sha256:`)
- uv verifies these checksums on install. If a wheel hash doesn't match, it errors out

## Markers

`dependencies` list shows the direct dep, and can include markers:

```toml
dependencies = [
    { name = "importlib-metadata", marker = "python_version < '3.10'" },
]
```

The marker tells uv to only install that dep when the condition is true. I checked `chardet` and saw markers for OS-specific deps too: `sys_platform == 'win32'`.

## What I noticed

- The lockfile is sorted alphabetically by package name. Not by dependency depth or install order.
- `requires-python` appears once in `[metadata]`, not per-package.
- No comments in the file — uv doesn't write inline docs.
- Running `uv lock` again produced the same hashes for the same versions. Reproducible.

Next time I want to compare lockfiles from different platforms to see how markers change the resolved set.
