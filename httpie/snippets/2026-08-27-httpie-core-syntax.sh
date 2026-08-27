#!/usr/bin/env bash
# last_verified: 2026-08-27 - httpie 3.2.4

# GET with query params and raw JSON number
http GET https://api.example.com/users user=alice status:=200

# POST with JSON body, custom headers, and auth
http POST https://api.example.com/users \
  name=Alice \
  active:=true \
  X-Request-Id:abc123 \
  Authorization: Bearer tok_123

# Download and save response body
http GET https://api.example.com/avatar.png > photo.png
