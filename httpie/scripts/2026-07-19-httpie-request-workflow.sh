#!/usr/bin/env bash
# last_verified: 2026-07-19 - httpie n/a

# Trying httpie for a typical API workflow: GET, POST, JSON body, custom headers, and --check-status

echo "=== GET a single post ==="
# --check-status makes this fail on 4xx/5xx so I can catch errors in scripts
http --check-status GET https://jsonplaceholder.typicode.com/posts/1

echo ""
echo "=== POST with key=value pairs (auto-JSON) ==="
# httpie turns key=value into a JSON body automatically
http POST https://jsonplaceholder.typicode.com/posts title="my title" body="post body" userId=1

echo ""
echo "=== POST with raw JSON body ==="
# Using --raw when I already have the JSON ready from elsewhere
http POST https://jsonplaceholder.typicode.com/posts \
  --raw '{"title": "raw json", "body": "sent via --raw", "userId": 2}'

echo ""
echo "=== Custom headers with Authorization ==="
# Headers use colon syntax; httpie strips them from the output body
http GET https://jsonplaceholder.typicode.com/posts/1 \
  Authorization:"Bearer fake-token-abc" \
  X-Trace-ID:"req-456"

echo ""
echo "=== Verbose output to inspect request/response ==="
# -v shows both request and response headers; useful for debugging
http -v GET https://jsonplaceholder.typicode.com/posts/1

echo ""
echo "=== Handling a 404 with --check-status ==="
# This exits non-zero; trying it in a subshell so the script keeps going
http --check-status GET https://jsonplaceholder.typicode.com/posts/99999 \
  && echo "OK" || echo "Expected 404 caught by --check-status"
