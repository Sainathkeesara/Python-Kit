---
last_verified: 2026-09-09
tool_version: "1.9.4"
sources:
  - https://pypi.org/project/bandit/
  - https://bandit.readthedocs.io/en/latest/start.html
---

# 2026-09-09 — Bandit severity and confidence scoring: a quickstart debrief

I followed the bandit quickstart again this week and the thing that kept tripping me up was the difference between severity and confidence — and how the short flags combine. Here's what I wish I'd known on day one.

## Severity: how bad is the finding

Bandit labels every finding LOW, MEDIUM, or HIGH. The flags stack by letter count:

- `-l` — LOW and above (basically everything)
- `-ll` — MEDIUM and above
- `-lll` — HIGH only

The trap: `-ll` still shows medium-severity issues, so if your team policy is "zero warnings", `-ll` is not enough — you want `-lll` or the clearer long form `--severity-level=high`. I now always use the long form in CI configs because the short flags are easy to miscount.

## Confidence: how sure is bandit

Confidence works the same way, with `-i`, `-ii`, `-iii`:

- `-i` — LOW confidence and above
- `-ii` — MEDIUM and above
- `-iii` — HIGH only

Combining them is additive: `-ll -ii` means "MEDIUM severity AND MEDIUM confidence or higher". A finding has to clear *both* thresholds to show up. This is useful for cutting noise — bump both to `-iii` for a strict gate, or keep `-ll -ii` for a first-pass report.

## Baseline files need extras and a clean tree

Generating a baseline (`bandit -f json -o baseline.json -r .`) and then comparing (`bandit -b baseline.json -r .`) is the right workflow for growing codebases, but two things catch people:

- The `bandit[baseline]` extra must be installed, otherwise you get `ModuleNotFoundError: No module named 'git'` — the baseline command shells out to git.
- The baseline subcommand requires a clean working directory. Commit or stash first.

## Inline suppression is one line only

`# nosec` on a line silences just that line — not the file. Beginners sometimes drop it at the top of a file expecting it to apply everywhere. For whole-file exclusions, use `--skip` with test IDs or the `skips` list in a config file. `--exclude` skips *directories*, which is a different thing entirely and easy to confuse with `--skip`.

## What I'd try next

I want to wire a severity/confidence gate into a pre-commit hook and see how the noise changes as the baseline grows. After that, comparing JSON output between `bandit[toml]` config and CLI flags to see which is easier to keep consistent across contributors.