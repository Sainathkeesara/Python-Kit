---
last_verified: 2026-08-05
tool_version: n/a
---

# Rich quickstart — what tripped me up

> I followed the official Rich quickstart and hit a few snags along the way. Here's what stuck.

## What I tried

I installed Rich and opened the quickstart guide. The first thing I noticed is that everything goes through `Console` — you don't just `print()` anymore, you create a `Console` instance and call `.print()` on it. That was a small mental shift.

## What tripped me up

### Inline markup vs ANSI codes

The quickstart uses inline markup like `[bold green]hello[/bold green]` and I kept forgetting to close the brackets. I'd write `[bold green]hello` and the terminal just showed the raw brackets. I had to keep reminding myself that every opening tag needs a closing tag — it's like HTML but simpler.

### Table column alignment

When I first created a Table, I didn't set `justify` on my columns and everything looked off. The default is left-aligned, but numbers look weird that way. I had to go back and add `justify="right"` for numeric columns. The quickstart shows this but I skipped over it on first read.

### Live display and refresh rate

I tried using `Live` for a progress display but set `refresh_per_second` too low and the output looked jerky. The default is 4, which felt right for most things. I also didn't realize that `Live` needs a `Console` instance — I was passing a plain string at first and got confused about why nothing updated in place.

### Console width detection

My terminal is wide but Rich kept wrapping output. Turns out Rich detects terminal width at the time the Console is created. If you resize your terminal after creating the Console, it doesn't auto-adjust. I had to recreate the Console or pass a explicit `width` parameter.

## What worked smoothly

The `Panel` and `Table` APIs were straightforward once I got the syntax down. The `progress` bar via `track()` was the easiest part — just wrap your iterable and go. The quickstart does a good job of showing the minimal path to get something looking decent.

## What I'd try next

I want to dig into `Renderable` objects and how custom renderables work. I also want to try the `rule()` and `columns()` layout helpers for building more complex terminal dashboards.
