#!/usr/bin/env bash
# last_verified: 2026-08-26 - httpie 3.2.4
#
# multi-endpoint-smoke-runner.sh — reusable smoke-test runner for a set of
# HTTPie endpoints.  Reads a simple TOML-style config (endpoint + jq
# assertion) and reports pass/fail per endpoint with colored output.
#
# Usage:
#   ./multi-endpoint-smoke-runner.sh config.toml
#
# Config format (key=value pairs, one section per endpoint):
#   [endpoint.get_posts]
#   method = "GET"
#   url    = "https://jsonplaceholder.typicode.com/posts"
#   assert = ". | length > 0"
#
# Requirements: bash ≥4, httpie 3.2.4, jq

set -euo pipefail

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
RESET='\033[0m'

section_label() { printf '\n%b== %s ==%b\n' "$BOLD" "$1" "$RESET"; }

# ---------------------------------------------------------------------------
# run_endpoint METHOD URL ASSERT_JQ TIMEOUT
#
# Calls httpie with CI-safe flags.  Pipes the JSON body through jq to
# evaluate ASSERT_JQ.  Returns 0 on pass, 1 on assertion failure, and
# forwards the httpie exit code on transport errors.
# shellcheck disable=SC2317
# run_endpoint is invoked indirectly via run_section -> eval; SC2317 is a
# false positive for this call pattern.
# ---------------------------------------------------------------------------
run_endpoint() {
  local method="$1" url="$2" assert="$3" timeout="${4:-30}"
  local response rc

  response=$(http --ignore-stdin --quiet --check-status --timeout "$timeout" \
               "$method" "$url" 2>&1) && rc=0 || rc=$?

  if (( rc != 0 )); then
    local msg
    case "$rc" in
      2) msg="timeout after ${timeout}s" ;;
      3) msg="redirect (3xx): add --follow if this is expected" ;;
      4) msg="client error (4xx)" ;;
      5) msg="server error (5xx)" ;;
      *) msg="unexpected exit code $rc" ;;
    esac
    printf '  %b✗ %s — %s%b\n' "$RED" "$method $url" "$msg" "$RESET" >&2
    return "$rc"
  fi

  if printf '%s' "$response" | jq -e "$assert" >/dev/null 2>&1; then
    printf '  %b✓ %s%b\n' "$GREEN" "$method $url" "$RESET"
    return 0
  else
    printf '  %b✗ %s — jq assertion failed: %s%b\n' \
      "$RED" "$method $url" "$assert" "$RESET" >&2
    return 1
  fi
}

# shellcheck disable=SC2317
# run_section is called via eval in the main loop; SC2317 is a false positive.
# ---------------------------------------------------------------------------
# run_section SECTION_NAME
#
# Parses method, url, assert, and optional timeout from variables set by
# parse_config, then calls run_endpoint.
# ---------------------------------------------------------------------------
run_section() {
  local section="$1"
  local method url assert timeout

  # Extract values from the caller's variable assignments.
  eval 'method="$smoke_method"'
  eval 'url="$smoke_url"'
  eval 'assert="$smoke_assert"'
  eval 'timeout="${smoke_timeout:-30}"'

  section_label "$section"
  run_endpoint "$method" "$url" "$assert" "$timeout"
}

# ---------------------------------------------------------------------------
# parse_config CONFIG_FILE
#
# Reads a simple key=value config and emits bash variable assignments on
# stdout.  Sections become calls to run_section.  Keys are prefixed with
# `smoke_` to avoid collisions.
# ---------------------------------------------------------------------------
parse_config() {
  local file="$1" current_section=""

  while IFS= read -r line; do
    # Strip comments and leading/trailing whitespace.
    line="${line%%#*}"
    line="$(echo "$line" | xargs)"

    [[ -z "$line" ]] && continue

    if [[ "$line" =~ ^\[(.+)\]$ ]]; then
      # Close the previous section by emitting a run call.
      if [[ -n "$current_section" ]]; then
        printf 'run_section "%s"\n' "$current_section"
      fi
      current_section="${BASH_REMATCH[1]}"
    elif [[ "$line" =~ ^([a-zA-Z_][a-zA-Z0-9_]*)=(.*)$ ]] && [[ -n "$current_section" ]]; then
      local key="${BASH_REMATCH[1]}"
      local val="${BASH_REMATCH[2]}"
      # Strip surrounding quotes.
      val="${val#\"}" ; val="${val%\"}"
      val="${val#\'}" ; val="${val%\'}"
      printf 'smoke_%s=%s\n' "$key" "$(printf '%s' "$val" | sed 's/"/\\"/g')"
    fi
  done < "$file"

  # Emit the final section.
  if [[ -n "$current_section" ]]; then
    printf 'run_section "%s"\n' "$current_section"
  fi
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if [[ $# -lt 1 ]]; then
  printf 'Usage: %s <config-file>\n' "$(basename "$0")" >&2
  exit 2
fi

CONFIG_FILE="$1"
if [[ ! -f "$CONFIG_FILE" ]]; then
  printf 'Config not found: %s\n' "$CONFIG_FILE" >&2
  exit 2
fi

PASS=0 FAIL=0

# eval the parsed config so run_section calls execute inline and can
# capture PASS/FAIL via the return value of run_endpoint.
while IFS= read -r cmd; do
  if [[ "$cmd" == run_section* ]]; then
    if eval "$cmd"; then
      (( ++PASS ))
    else
      (( ++FAIL ))
    fi
  elif [[ -n "$cmd" ]]; then
    eval "$cmd"
  fi
done < <(parse_config "$CONFIG_FILE")

section_label "summary"
printf '  pass=%d  fail=%d  total=%d\n' "$PASS" "$FAIL" $((PASS + FAIL))

if (( FAIL > 0 )); then
  printf '%b✗ smoke test: %d endpoint(s) failed%b\n' "$RED" "$FAIL" "$RESET" >&2
  exit 1
fi
printf '%b✓ all endpoints passed%b\n' "$GREEN" "$RESET"
exit 0
