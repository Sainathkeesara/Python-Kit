# More pipdeptree patterns I figured out

I already knew `pipdeptree --json` and `--exclude`. Today I tried a few more.

## --graph-output

```bash
pipdeptree --graph-output dot > tree.dot
```

Lets you export in dot, flat, json, or png format (if you have graphviz). I used dot + `dot -Tsvg tree.dot -o tree.svg` to render a proper graph. The flat output is a simple indented list, less pretty than the default but better for grepping.

## --local-only

```bash
pipdeptree --local-only
```

Hides system-site-packages. I work inside venvs so this didn't change much for me, but if you have `--system-site-packages` enabled it makes the output manageable.

## --python-version

```bash
pipdeptree --python-version 3.12
```

Lets you target a specific Python version. I tested this — it uses the most recent compatible versions of each package for that Python. Useful if you maintain a library that needs to support an older Python.

## --all

```bash
pipdeptree --all
```

By default pipdeptree skips packages it considers "outdated" or "non-functional." `--all` shows everything. I compared outputs — mostly the same, but `--all` included some pip-internal packages that were normally hidden.

## Combining flags

My go-to pattern now:

```bash
pipdeptree --json --local-only --exclude setuptools,wheel,pip-pkgs > deps.json
```

Gives me a clean JSON I can pass to my parse scripts.
