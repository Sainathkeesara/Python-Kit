# pipdeptree quickstart follow-up — visualizing deps and detecting cycles

I went through the official pipdeptree quickstart guide today. Here's what I learned and where I got stuck.

## What I did

Installed pipdeptree and ran it on the project's environment:

```bash
uv tool install pipdeptree
pipdeptree
```

Then I checked the JSON output:

```bash
pipdeptree --json > deps.json
```

And looked for cycles:

```bash
pipdeptree --warn cycle
```

## What tripped me up

- The `--warn cycle` flag doesn't just warn — it lists every cycle it finds. On a real project this can be huge. I'd suggest piping to a file or using `--exclude` to filter down.
- `--packages` filters by package name, but it's case-sensitive on some platforms. I typed `pipdeptree --packages Requests` and got nothing. Lowercase `requests` worked.
- The JSON output is an array of objects, each with `package`, `dependencies`, and `required_version`. The `dependencies` key is a list — I initially expected a dict keyed by package name.
- There's a confusing callout in the docs about `--freeze` vs regular output. `--freeze` gives you a flat list like `pip freeze` but without pipdeptree's tree logic. Don't use it if you want hierarchy.
- When I piped JSON to `jq` to extract leaf packages, empty arrays weren't being caught. `dependencies | length == 0` is the correct test, not `dependencies == null` or `dependencies == []`.

## Verify

Look at deps.json and confirm:
- Cycle entries show up under `** Cycle **` headers in text mode.
- JSON mode lists every package with its full dependency tree.
- Leaf packages have empty `dependencies` arrays.
