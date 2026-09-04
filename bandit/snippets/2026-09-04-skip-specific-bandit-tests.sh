# last_verified: 2026-09-04 · bandit 1.9.4

# Ran a bandit scan over a test file and got flagged on every assert for
# B101 (assert_used). The asserts are the whole point of the file. Asked
# myself: how do I tell bandit "skip these specific checks for this one
# file" without losing the rest of the scan?

bandit -r src/ -s B101,B105

# That's it. -s takes a comma-separated list of test IDs to skip. B101 is
# the assert-in-test-files one, B105 is the hardcoded-password-string one
# that fires on anything resembling "password = 'secret'". I only needed
# B101 here, but I included B105 to show the comma syntax.
#
# Useful test IDs I keep handy:
#   B101  assert_used
#   B102  exec_used
#   B105  hardcoded_password_string
#   B301  pickle
#   B403  import_pickle
#
# If I wanted to skip just one file, I'd use --exclude, but for blanket
# class-of-tests this is faster than writing a .bandit config file.