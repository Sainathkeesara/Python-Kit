# Trying rich progress bar — simplest approach first
from rich.progress import track
import time

# track() wraps an iterable with a progress bar — dead simple
for _ in track(range(10), description="Working..."):
    time.sleep(0.3)
