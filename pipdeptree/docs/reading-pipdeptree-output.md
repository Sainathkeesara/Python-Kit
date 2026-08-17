---
last_verified: 2026-08-17
tool_version: n/a
---

# Reading pipdeptree output: trees, reverse deps, and the --warn conflict flags

## Purpose

This doc explains how to read the three pipdeptree output modes that matter most when auditing a dependency tree: the default text tree, JSON for programmatic inspection, and reverse-dependency listings. It also covers the `--warn` flag modes that surface hidden conflicts and cycles.

## Prerequisites

- pipdeptree installed in the active virtual environment.
- A project with at least a few installed packages so the tree is non-empty.

## Reading the default tree

Running `pipdeptree` with no flags prints a text tree. The indentation shows depth: top-level packages have no indent, their dependencies are indented one level, and so on. Version numbers appear after `==` or `[` on the package line. Conflicts show up as shared child nodes with two different parent lines pointing at the same version — this is the visual cue that two parents require incompatible versions.

A useful first pass is to pipe the tree through a filter:

```bash
pipdeptree | grep -E "requests|urllib3"
```

This narrows the output to the subtree around a known package without changing the tree structure.

## Reading JSON output

`--json` converts the tree into a structured array. Each entry has a `package` object and a `dependencies` array. This format is what scripts parse when they need to classify packages, count leaf nodes, or export to another format.

```bash
pipdeptree --json > deps.json
```

Inside the JSON, a leaf package is an entry whose `dependencies` array is empty. A top-level package is one that no other entry lists in its `dependencies` array. The JSON shape makes these distinctions easy to verify with a short Python loop, but the same classification is possible with `jq` if you prefer shell tools.

## Reverse dependencies

`--reverse` flips the tree so that dependents appear before the packages they depend on. This is the fastest way to answer "who needs this package?" without scanning the full tree manually.

```bash
pipdeptree --reverse --packages requests
```

The `--packages` filter is important here: without it, the reverse tree dumps every package and is hard to read. With `--packages`, pipdeptree trims the output to just the subtree where `requests` appears as a dependency.

## --warn modes

The `--warn` flag changes what pipdeptree prints and whether it exits non-zero. The modes that matter for reading output are:

- `silence` — suppress all warning blocks. Useful when the tree is being piped to a parser and warning noise would break downstream tools.
- `cycle` — list dependency cycles. Cycles are packages that indirectly depend on themselves, and they often indicate version-pinning mistakes or duplicated namespace packages.
- `fail` — exit with a non-zero status if any warning is found. This is the CI-friendly mode because it turns the tree inspection into a gate that a script can branch on.

```bash
pipdeptree --warn fail
```

When `--warn fail` triggers, the exit code is non-zero, but the stdout still contains the full tree plus the warning details. Capture both the output and the exit status so you can log what failed.

## Verify

Run these commands against any active virtual environment:

```bash
# 1. Confirm the text tree is readable and shows depth
pipdeptree | head -20

# 2. Confirm JSON parses cleanly
pipdeptree --json > /tmp/deps.json
python3 -c "import json; json.load(open('/tmp/deps.json'))"

# 3. Confirm reverse tree for a known package
pipdeptree --reverse --packages pipdeptree

# 4. Confirm --warn fail exits non-zero when warnings exist
pipdeptree --warn fail; echo "exit=$?"
```

Step 4 should return a non-zero exit code on most real projects because version conflicts are common. The exact exit value depends on the warning type, but anything other than `0` means the gate fired.
