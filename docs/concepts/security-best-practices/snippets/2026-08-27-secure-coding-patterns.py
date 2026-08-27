# last_verified: 2026-08-27 · n/a

"""
I collected these patterns after reading about common Python security
mistakes. Each one is a small, self-contained example showing the
safe version alongside the risky version so I can spot the difference.

Covers:
- Parameterized queries (prevent SQL injection)
- Input allowlisting (reject bad data before processing)
- CSPRNG usage (secrets module for tokens/passwords)
- Secrets handling (env vars, no hardcoded keys)
"""

import hashlib
import hmac
import os
import re
import secrets
import sqlite3
from typing import Any


# --- 1. Parameterized queries ---

def unsafe_query(user_input: str) -> list[dict[str, Any]]:
    """DON'T do this — string formatting in SQL lets attackers inject anything."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    # This is vulnerable: user_input goes straight into the query string
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    # conn.execute(query)  # blocked — would run the injected SQL
    conn.close()
    return []


def safe_query(user_input: str) -> list[dict[str, Any]]:
    """DO this — parameterized queries let the DB driver escape properly."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("CREATE TABLE users (name TEXT, role TEXT)")
    # The ? placeholder is replaced safely by sqlite3 — no injection possible
    rows = conn.execute(
        "SELECT * FROM users WHERE name = ?", (user_input,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# --- 2. Input allowlisting ---

# The research flagged: input validation — rejecting data that doesn't match
# expected types and ranges before processing. Allowlisting is stricter
# than blocklisting because you only accept what you know is safe.

ALLOWED_ROLES = {"admin", "editor", "viewer"}
EMAIL_RE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def validate_user_input(name: str, role: str, email: str) -> tuple[bool, list[str]]:
    """Check each field against an allowlist. Returns (is_valid, errors)."""
    errors: list[str] = []

    if not name or len(name) > 100:
        errors.append("name must be 1-100 characters")

    if role not in ALLOWED_ROLES:
        errors.append(f"role must be one of {ALLOWED_ROLES}, got '{role}'")

    if not EMAIL_RE.fullmatch(email):
        errors.append(f"invalid email: {email}")

    return (len(errors) == 0, errors)


# --- 3. CSPRNG usage ---

def generate_api_key() -> str:
    """Generate a cryptographically secure API key.

    secrets module uses the OS CSPRNG (/dev/urandom on Linux, CryptGenRandom
    on Windows). Never use random.random() or random.randint() for security
    tokens — they're predictable.
    """
    return secrets.token_urlsafe(32)


def generate_totp_secret() -> str:
    """Generate a base32 secret for TOTP (Google Authenticator style)."""
    return secrets.token_hex(20)


def hash_password(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    """Hash a password with PBKDF2-HMAC-SHA256.

    Always use a salt — two identical passwords produce different hashes.
    The research notes: never store plaintext passwords; always hash with
    a slow, salted algorithm.
    """
    if salt is None:
        salt = secrets.token_bytes(16)
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations=260_000)
    return key, salt


def verify_password(password: str, stored_hash: bytes, salt: bytes) -> bool:
    """Verify a password against its stored hash."""
    computed, _ = hash_password(password, salt)
    # Use hmac.compare_digest to prevent timing attacks
    return hmac.compare_digest(computed, stored_hash)


# --- 4. Secrets handling ---

def get_api_key() -> str:
    """Load secrets from environment variables — never hardcode them.

    The research flagged: a leaked API key in a public repo is one of the
    most common security incidents. Environment variables keep secrets out
    of source code.
    """
    key = os.environ.get("API_KEY")
    if not key:
        raise RuntimeError("API_KEY environment variable not set")
    return key


# The before/after from the security primer shows this clearly:
#
# BEFORE — vulnerable:
#   API_KEY = "sk-live-abc123"          # hardcoded
#   result = eval(user_data)            # arbitrary execution
#
# AFTER — safer:
#   API_KEY = os.environ["API_KEY"]     # from environment
#   if not re.fullmatch(r"\d+", data):  # validate first
#       raise ValueError("digits only")
#   result = int(data)


# --- demo ---

if __name__ == "__main__":
    # Parameterized query
    print("Safe query result:", safe_query("admin"))

    # Input validation
    valid, errors = validate_user_input("Alice", "admin", "alice@example.com")
    print(f"Valid: {valid}, errors: {errors}")

    valid2, errors2 = validate_user_input("", "superuser", "not-an-email")
    print(f"Valid: {valid2}, errors: {errors2}")

    # CSPRNG
    print(f"API key: {generate_api_key()}")
    print(f"TOTP secret: {generate_totp_secret()}")

    # Password hashing
    pw_hash, salt = hash_password("my-secret-password")
    print(f"Password verified: {verify_password('my-secret-password', pw_hash, salt)}")
    print(f"Wrong password verified: {verify_password('wrong', pw_hash, salt)}")
