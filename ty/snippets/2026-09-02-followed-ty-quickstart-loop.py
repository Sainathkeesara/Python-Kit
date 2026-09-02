# last_verified: 2026-09-02 · ty n/a
"""Following the ty quickstart: minimal typed module + the type-check loop.

I installed ty, wrote this tiny module, and ran `ty check` on it after
every edit. The loop below is what I actually used — check, fix, re-check.
"""

from typing import TypeVar

T = TypeVar("T")


def add(a: int, b: int) -> int:
    # docs example used plain ints; keeping it minimal on purpose
    return a + b


def first(items: list[T]) -> T:
    # tried items[0] without the Generic import first and ty flagged
    # the unbound TypeVar, so I added the TypeVar at the top
    return items[0]


total: int = add(2, 3)
print(total)

names = ["ada", "grace"]
print(first(names))

# reveal_type only exists inside the type checker, so running this file
# with plain python blew up with NameError on my first try. This fallback
# keeps `python file.py` working; ty still reports the static types.
try:
    reveal_type
except NameError:
    def reveal_type(obj):  # type: ignore[no-redef]
        print(type(obj).__name__, obj)
        return obj

reveal_type(total)
reveal_type(first(names))

# What I'd try next: annotate a second file that imports this one and
# see whether ty follows the import without extra flags.
#
# The type-check loop I ran while writing this:
#   ty check ty/snippets/2026-09-02-followed-ty-quickstart-loop.py
# Got stuck on: running `ty` with no path checked the whole repo and the
# output was noisy — passing the file path kept the loop tight.
