#!/usr/bin/env bash
# tried-uv-lock-reproducibility.sh — test that uv.lock checksums are stable
# Procedure: init project → add dep → lock → re-lock → diff

PROJECT_DIR=$(mktemp -d)
cd "$PROJECT_DIR" || exit 1

uv init --no-readme test-repro > /dev/null 2>&1
uv add requests > /dev/null 2>&1

cp uv.lock uv.lock.baseline

# Lock again from scratch — checksums should be identical
uv lock > /dev/null 2>&1

if diff uv.lock uv.lock.baseline > /dev/null 2>&1; then
    echo "PASS: uv.lock is reproducible across lock commands"
else
    echo "FAIL: uv.lock changed on re-lock — checksum instability detected"
    diff uv.lock uv.lock.baseline
    exit 1
fi

rm -rf "$PROJECT_DIR"
