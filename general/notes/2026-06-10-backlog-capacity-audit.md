# Backlog capacity audit

I counted open vs completed ACTIVE tasks per tool in tasks.md to figure out where we're bottlenecked.

## Counts

| Tool | Open | Completed | Total |
|------|------|-----------|-------|
| General | 10 | 2 | 12 |
| Ruff | 4 | 0 | 4 |
| pytest | 4 | 2 | 6 |
| mypy | 4 | 3 | 7 |
| py-spy | 4 | 1 | 5 |
| httpie | 4 | 0 | 4 |
| typer | 1 | 0 | 1 |
| pre-commit | 4 | 0 | 4 |
| Ty | 4 | 0 | 4 |
| pipdeptree | 3 | 2 | 5 |
| uv.lock | 3 | 2 | 5 |
| uv | 2 | 0 | 2 |
| pip-audit | 2 | 0 | 2 |
| tox | 2 | 0 | 2 |
| rich | 2 | 0 | 2 |
| pyproject.toml | 2 | 1 | 3 |

Total: 53 open, 13 completed across 16 tools.

## Next-level blockers

Per the unlock deps in TOOL_HIERARCHY.md, uv and Ruff are the two L1 gateways. Both are at L1 with incomplete L1 task lists — uv has 2 open tasks, Ruff has 4. Until those tools finish L1, the locked tools (mypy, pre-commit, pip-audit, Ty, rich, typer, pipdeptree, py-spy, httpie, tox) won't unlock.

Most open tasks are notes. A handful are snippets or config files. The backlogs with the most unstarted work are General (10 — mostly project/docs tasks) and then a cluster of tools at 4 each.

I should focus on finishing uv and Ruff's remaining L1 tasks to unlock the next wave.
