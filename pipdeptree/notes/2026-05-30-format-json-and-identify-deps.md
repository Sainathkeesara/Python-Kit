# pipdeptree JSON output and dependency types

Today I learned how to get pipdeptree output in JSON format and how to distinguish between top-level and transitive dependencies.

## What is pipdeptree JSON output?

Running `pipdeptree --json` outputs a JSON array of objects, each representing a package. Each object has:
- `package`: the package name
- `installed_version`: the version installed
- `dependencies`: a list of dependencies (each with `package` and `installed_version`)

## Top-level vs transitive dependencies

Top-level dependencies are those that are directly installed by the user (or via requirements.txt) and appear in the root of the dependency tree. Transitive dependencies are those that are pulled in by top-level dependencies.

In the JSON output, we can identify top-level dependencies by checking if they are listed as a dependency of another package. If a package is not in the `dependencies` list of any other package, it is a top-level dependency.

Example: 
- If we have `requests` as a top-level dependency, and `requests` depends on `urllib3`, then `urllib3` is transitive.

In the JSON output from the /work project, we saw that packages like `uv`, `Ruff`, and `pytest` are top-level (they are not dependencies of any other package in the tree), while their dependencies (like `pip` for `uv`, or `platformdirs` for `Ruff`) are transitive.