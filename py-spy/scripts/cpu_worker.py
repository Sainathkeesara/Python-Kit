#!/usr/bin/env python3
"""Minimal CPU-bound workload for py-spy profiling practice."""

def do_math():
    for i in range(1_000_000):
        _ = i * i + i // 2

def do_strings():
    parts = []
    for i in range(50_000):
        parts.append(f"item-{i}")
    return ",".join(parts)

if __name__ == "__main__":
    do_math()
    do_strings()
    print("done")
