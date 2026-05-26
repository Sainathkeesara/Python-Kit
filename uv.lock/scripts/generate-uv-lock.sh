#!/usr/bin/env bash
# Generate a uv.lock by creating a project and syncing dependencies

uv init --app demo-lockfile
cd demo-lockfile || exit 1
uv add requests
echo "--- uv.lock generated ---"
head -30 uv.lock
echo "--- total packages ---"
grep -c '^name' uv.lock
