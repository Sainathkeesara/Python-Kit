#!/usr/bin/env bash
# last_verified: 2026-09-04 · tox n/a
# Run tox across every pyenv Python version and record a pass/fail matrix.

echo "python_version,status" > tox-matrix.csv
for ver in $(pyenv versions --bare 2>/dev/null); do
  env="py$(echo "$ver" | cut -d. -f1-2 | tr -d .)"
  tox -e "$env" >/dev/null 2>&1 && status=PASS || status=FAIL
  echo "$ver,$status" >> tox-matrix.csv
done
cat tox-matrix.csv
