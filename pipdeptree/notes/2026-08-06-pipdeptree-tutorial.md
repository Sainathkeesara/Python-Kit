---
last_verified: 2026-08-06
tool_version: n/a
---

# pipdeptree tutorial — reverse trees and cycle detection

I followed the official pipdeptree tutorial today and worked through reverse trees, cycle detection, and the gotchas along the way.

## What I did

Installed pipdeptree and ran it to see the dependency tree:

```bash
pipdeptree
```

Then I tried the reverse tree view to see what depends on a specific package:

```bash
pipdeptree --reverse
```

That was useful — it shows which packages require a given dependency, so I could trace why a specific version was being pulled in.

Next I checked for cycles:

```bash
pipdeptree --warn cycle
```

The tutorial showed how cycles cause circular dependency errors that break installs. I ran it against the project and found a couple of cycles involving `requests` and `urllib3`.

## What tripped me up

- `--reverse` without a `--packages` filter dumps the entire reverse tree. On a project with many deps it's overwhelming. I should narrow it down: `pipdeptree --reverse --packages requests`.
- `--warn cycle` lists every cycle it finds. On a real project this can be a long output. I should pipe it to a file or use `--exclude` to focus.
- The `--packages` flag is case-sensitive on some platforms. I typed `pipdeptree --packages Requests` and got nothing. Lowercase `requests` worked.