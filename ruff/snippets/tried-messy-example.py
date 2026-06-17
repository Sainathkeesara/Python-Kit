# Deliberately messy — see what Ruff catches
import os, sys, json  # multiple imports on one line

def process(data):
    x = 1  # unused variable
    print("this line is intentionally really really really really really really really really really really really really really long")
    return data

name = 'Alice'
greeting = "Hello"  # inconsistent quotes

if __name__ == "__main__":
    process(undefined_variable)  # undefined name
