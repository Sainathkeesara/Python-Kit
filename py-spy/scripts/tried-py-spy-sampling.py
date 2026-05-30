# Script for py-spy to sample — run this then point py-spy at its PID
#   py-spy top --pid $(pgrep -f tried-py-spy-sampling)
#   py-spy record -o flame.svg --pid $(pgrep -f tried-py-spy-sampling) --duration 10

import os
import time

def do_math(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def do_strings(n):
    result = ""
    for i in range(n):
        result += chr(65 + i % 26)
    return result

print(f"py-spy sampling target PID: {os.getpid()}")
while True:
    do_math(50000)
    do_strings(30000)
    time.sleep(0.2)
