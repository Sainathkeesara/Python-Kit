# Installed Ty and rendered my first markdown file

I read the Ty primer earlier — it's a Rust-based markdown renderer from the Astral team (same folks behind uv and Ruff). Today I actually installed it and tried it out.

## Install

The Ty docs recommend `uv tool install ty`:

```
uv tool install ty
```

That installed the `ty` binary globally. Confirmed with `ty --version` — got 0.0.39.

## First render

Created a simple markdown file `test.md`:

```markdown
# Hello

This is **bold** and *italic*.

- item one
- item two
```

Rendered it:

```
ty render test.md
```

The output looked great — colored headers, bold text rendered as bold (bright white), lists with proper bullet alignment. It rendered straight to the terminal without any extra config.

## What I tried next

- `ty render --width 60 test.md` — sets a narrower column width. Useful for READMEs with long lines.
- `ty render --theme github-dark test.md` — switches the color palette. Has a few built-in themes.
- `ty render --pager` — opens in a pager (less) for long files.

## What tripped me up

- Running `ty` without a subcommand drops into interactive mode, not a help page. That was confusing at first.
- `ty --help` shows the available subcommands: `check`, `render`, `format`. I only cared about `render` today.
- The CSS theme file from the config is only for `ty render` output, not for `ty check`.
- Ty is NOT a type checker despite sharing the same name space — `ty check` is the actual type checker, `ty render` is the markdown feature.

## Next

I'll try `ty format` on a markdown file to see if it auto-fixes formatting, and experiment with custom CSS themes.
