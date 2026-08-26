#!/usr/bin/env bash
# last_verified: 2026-08-26 - httpie 3.2.4
#
# ci-httpie-wrapper.sh — sourceable bash library that wraps `http` (HTTPie)
# with CI-safe defaults so scripts don't hang on stdin, fail loudly on bad
# status codes, and surface readable error messages.
#
# Source it from any CI script:
#   source "$(dirname "$0")/ci-httpie-wrapper.sh"
#
# Requirements: bash ≥4, httpie 3.2.4, jq

# ---------------------------------------------------------------------------
# Status-code → human-readable message map for --check-status exit codes.
# ---------------------------------------------------------------------------
_httpie_status_map() {
  case "$1" in
    2) echo "timeout: the server did not respond within the request window" ;;
    3) echo "redirect (3xx): follow redirects with --follow, or treat as success" ;;
    4) echo "client error (4xx): check the request path, headers, and body" ;;
    5) echo "server error (5xx): the upstream service is failing — retry or escalate" ;;
    *) echo "unexpected exit code $1 from httpie --check-status" ;;
  esac
}

# ---------------------------------------------------------------------------
# httpie_request METHOD URL [KEY=VALUE ...]
#
# Wraps `http` with CI-safe defaults:
#   --ignore-stdin  prevents hangs when stdin is not a terminal (CI, cron)
#   --quiet         suppresses the progress bar and status line
#   --check-status  turns non-2xx into a non-zero exit
#   --timeout 30    caps the request at 30 s
#
# Returns the response body on stdout.  On failure, prints a readable
# message to stderr and exits with the original httpie exit code.
# ---------------------------------------------------------------------------
httpie_request() {
  local method="$1"; shift
  local url="$1"; shift
  local body
  local rc

  body=$(http --ignore-stdin --quiet --check-status --timeout 30 \
            "$method" "$url" "$@" 2>&1) && rc=0 || rc=$?

  if (( rc == 0 )); then
    printf '%s' "$body"
  else
    local msg
    msg=$(_httpie_status_map "$rc")
    printf 'httpie_request FAILED (%s %s): %s\n' "$method" "$url" "$msg" >&2
    # Re-emit the raw body so the caller can inspect it in CI logs.
    printf '%s\n' "$body" >&2
    exit "$rc"
  fi
}

# ---------------------------------------------------------------------------
# httpie_json_field JSON_PATH [KEY=VALUE ...]
#
# Calls httpie_request and pipes the JSON body through jq, returning
# the value at JSON_PATH (e.g. '.id' or '.[] | .name').
# Exits 1 if jq cannot extract the path or the response is not valid JSON.
# ---------------------------------------------------------------------------
httpie_json_field() {
  local jq_path="$1"; shift
  local response

  response=$(httpie_request "$@") || exit $?

  printf '%s' "$response" | jq -e "$jq_path" 2>/dev/null || {
    printf 'httpie_json_field: jq failed for path "%s" on response:\n%s\n' \
      "$jq_path" "$response" >&2
    exit 1
  }
}

# ---------------------------------------------------------------------------
# httpie_json_parse KEY=VALUE ...
#
# Returns the parsed JSON body from httpie_request as a string.
# Useful when you need the full object for multiple jq queries.
# ---------------------------------------------------------------------------
httpie_json_parse() {
  httpie_request "$@"
}
