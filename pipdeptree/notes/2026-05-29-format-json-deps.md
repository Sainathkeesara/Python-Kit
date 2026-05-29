# Formatting pipdeptree output as JSON

I ran `pipdeptree --json` on the /work project to get the dependency tree as structured data instead of the default text tree.

## What I saw

The JSON output is a list of objects, each with:
- `package_name` — name of the package
- `installed_version` — version string
- `dependencies` — list of nested objects with the same shape

This is way easier to parse than the text tree if I want to script something around it.

## Top-level vs transitive

The packages at the top level of the JSON array are the ones I installed directly. Any package that only appears as a nested item under someone else's `dependencies` is transitive.

So if `requests` is in the top-level list and `urllib3` only shows up under `requests.dependencies`, I know `urllib3` was pulled in automatically — I didn't choose it.

## Filtering by package

I also tried `pipdeptree --packages requests` which trims the tree to just show `requests` and its subtree. Handy when you only care about one package's dependency chain.

## What I'd try next

I want to write a small script that filters `pipdeptree --json` output and extracts just the top-level packages, maybe dump them into a pip-compile compatible format.
