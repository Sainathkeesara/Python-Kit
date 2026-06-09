#!/usr/bin/env bash
# Pipe markdown through ty and capture formatted output
set -e

MD=$(cat <<'MARKDOWN'
# Hello from ty

This is **bold** and *italic* text.

- List item one
- List item two

> A blockquote for testing

```python
print("code block")
```
MARKDOWN
)

echo "=== Piping markdown to ty ==="
echo "$MD" | ty > formatted-output.txt 2>&1

echo "=== Captured output (first 20 lines) ==="
head -20 formatted-output.txt

echo ""
echo "=== Output saved to formatted-output.txt ==="
wc -l formatted-output.txt
