# pipdeptree — what tripped me up

I wanted to filter the tree to just one package. `pipdeptree -p requests` works but the output still shows transitive deps under it (which makes sense). I kept expecting `-p` to flatten.

The JSON output was confusing at first. Each entry has a `package` dict *and* a `dependencies` list — but the `dependencies` also have `package` dicts inside them. I kept trying `pkg["dependencies"]["package"]` until I printed one entry and saw the structure.

Missing deps: if pipdeptree can't resolve a dep, it shows `{"package": {"key": "missing-pkg", "installed_version": null}, "dependencies": []}`. Annoying when filtering — I had to add a `None` check on `installed_version`.
