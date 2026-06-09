#!/usr/bin/env bash
# Install HTTPie with pipx and try GET/POST against JSONPlaceholder

set -e

echo "=== Installing HTTPie via pipx ==="
pipx install httpie

echo ""
echo "=== GET /posts/1 ==="
http GET https://jsonplaceholder.typicode.com/posts/1

echo ""
echo "=== POST /posts ==="
http POST https://jsonplaceholder.typicode.com/posts/ title=foo body=bar userId=1
