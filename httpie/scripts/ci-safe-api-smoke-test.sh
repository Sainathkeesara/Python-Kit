#!/usr/bin/env bash
# last_verified: 2026-08-13 · httpie 3.2.4
# CI-safe API smoke test with httpie.
#
# The stdin trap: outside an interactive terminal (cron, CI, GitHub Actions)
# stdin is redirected, so httpie waits for a request body that never arrives
# and the job just hangs. Every http call below passes --ignore-stdin so the
# script runs to completion even when a CI runner feeds it a closed stdin.
#
# --check-status turns non-2xx responses into a non-zero exit code (2 on
# timeout, 3 on 3xx unless --follow, 4 on 4xx, 5 on 5xx, 6 on exceeding
# --max-redirects), so a bad response fails the CI step instead of printing a
# 500 body and silently passing.

set -euo pipefail

BASE_URL="${BASE_URL:-https://jsonplaceholder.typicode.com}"

echo "== 1. health check: GET /posts/1 must be 2xx and valid JSON =="
http --ignore-stdin --check-status --quiet GET "$BASE_URL/posts/1" | jq -e . >/dev/null

echo "== 2. shape check: /posts is a non-empty list =="
count=$(http --ignore-stdin --check-status --quiet GET "$BASE_URL/posts" | jq 'length')
[ "$count" -gt 0 ]

echo "== 3. create: POST /posts must succeed =="
http --ignore-stdin --check-status --quiet POST "$BASE_URL/posts" \
  title="smoke test" body="from CI" userId=1 >/dev/null

echo "== 4. negative: --check-status must fail a 404 =="
if http --ignore-stdin --check-status --quiet GET "$BASE_URL/posts/999999" >/dev/null 2>&1; then
  echo "FAIL: expected the 404 to be gated by --check-status"
  exit 1
fi

echo "== 5. output control: response headers only (-ph) =="
http --ignore-stdin --check-status -ph GET "$BASE_URL/posts/1"

echo "ALL SMOKE TESTS PASSED"
