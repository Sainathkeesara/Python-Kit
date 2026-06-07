# Deliberately messy Python file for Ruff testing
# This file contains various style violations to see what Ruff catches

import os, sys, json
from pathlib import Path

# Unused import
import unused_module

# Constant naming violation (should be UPPER_CASE)
my_constant_value = 42

# Short variable name
def f(x):
    # Line too long
    very_long_variable_name_here = "this line is way longer than the default 88 characters and should trigger E501 in most linters but we might ignore it"
    
    # Unused variable
    unused = x * 2
    
    # Undefined name (should trigger)
    print(undefined_variable)
    
    return x * 2

# Missing whitespace
result=f(5)

# Missing newlines at end of file (can't demonstrate in this format)