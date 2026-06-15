# Deliberately messy file — let's see what Ruff catches
# I threw in every bad habit I can think of

import os, sys, json  # multiple imports on one line

MY_CONSTANT = 42  # TODO: why does ruff flag this? oh wait it doesn't...

def process(data):
    x = 1  # unused variable
    # line too long below — this should trigger E501 if ruff enforces it
    print("this line is intentionally really really really really really really really really really really really really really long")
    return data

# inconsistent quotes
name = 'Alice'
greeting = "Hello"

if __name__ == "__main__":
    process(undefined_variable)  # this should definitely be flagged
