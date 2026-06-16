from typing import List

def longest(items: List[str]) -> str:
    return max(items, key=len)

short: List[str] = ["a", "bb", "ccc"]
print(longest(short))
