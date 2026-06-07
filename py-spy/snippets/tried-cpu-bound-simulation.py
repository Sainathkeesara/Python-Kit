# Simulate CPU-bound work for py-spy to sample
import os

def busy_loop(n):
    total = sum(i ** 2 for i in range(n))
    return total

print(f"PID: {os.getpid()}")
while True:
    busy_loop(200_000)
