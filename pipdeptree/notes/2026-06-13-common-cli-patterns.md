# pipdeptree CLI patterns I figured out

I keep going back to a few `pipdeptree` commands now that the JSON shape makes more sense.

The basic tree is still the fastest way to see what I have:

```bash
pipdeptree
```

When I only care about one package, I use `pipdeptree --packages requests`. It still prints the subtree, so it is not a flat "just this package" view. I expected it to be flatter at first.

For scripts, I use JSON:

```bash
pipdeptree --json > deps.json
```

Then I can loop over the top-level entries and their `dependencies` lists. Leaf packages are just entries where `dependencies` is empty.

A few patterns I use:
- `pipdeptree --exclude setuptools,wheel,pip` keeps the tree smaller.
- `pipdeptree --warn silence` hides warning noise when I only want the tree.
- `pipdeptree --warn cycle` shows dependency cycles, but it can be noisy.
- `pipdeptree --freeze` gives a flat requirements-style list, not a dependency tree.
- `pipdeptree --json --reverse` is useful when I want packages that depend on a target.

My current habit is text mode for quick reading and JSON for anything I want to parse.
