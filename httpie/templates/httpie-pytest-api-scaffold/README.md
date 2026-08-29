---
last_verified: 2026-08-29
tool_version: 3.2.4
sources:
  - https://httpie.io/docs/cli/scripting
  - https://httpie.io/docs/cli/usage
  - https://pypi.org/project/httpie/
---

# httpie-pytest-api-scaffold

Project scaffold: httpie + pytest integration test suite for a small FastAPI service with GitHub Actions CI wiring.

## Purpose

Provides a ready-to-clone starting point for API projects that use HTTPie as the HTTP client for integration testing. The scaffold includes a minimal FastAPI app, pytest tests that exercise the API through the `http` CLI (not through a Python test client), and a CI workflow that runs those tests on every push.

## When to use

Use this scaffold when building a new REST API and you want integration tests that hit the real HTTP stack — request serialisation, response parsing, status codes, and headers — rather than mocking the transport layer. HTTPie's `--check-status` flag turns unexpected status codes into test failures, which makes CI gating straightforward.

## Structure

```
.
├── src/
│   ├── __init__.py
│   └── app.py              # FastAPI sample service
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # fixtures: live server + httpie base_url
│   └── test_api.py         # integration tests via http CLI
├── .github/workflows/
│   └── ci.yml              # GitHub Actions matrix
├── pyproject.toml          # deps + tool config
└── README.md
```

## Prerequisites

- Python ≥ 3.10
- [httpie](https://httpie.io) 3.x (`pip install httpie` or `uv pip install httpie`)
- FastAPI + uvicorn (`pip install fastapi uvicorn`)
- pytest (`pip install pytest`)

## Quick start

```bash
# 1. Clone or copy this scaffold
cp -r httpie-pytest-api-scaffold my-api && cd my-api

# 2. Create a virtual environment and install deps
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# 3. Run the tests
pytest -v

# 4. Run the server manually (optional)
uvicorn src.app:app --reload
```

## How the tests work

`conftest.py` starts a uvicorn server on a free port in a background thread before each test session. Tests receive a `base_url` fixture and call the `http` CLI via `subprocess.run`. Each test asserts on status code, response body, and content-type — the same checks a CI script would perform.

```python
# Example test — see tests/test_api.py for the full suite
def test_list_items(base_url):
    result = subprocess.run(
        ["http", "--check-status", "--ignore-stdin", "GET", f"{base_url}/items"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    items = json.loads(result.stdout)
    assert isinstance(items, list)
```

## CI wiring

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs `pytest` on a Python version matrix. HTTPie is installed alongside the project dependencies so tests can invoke the `http` command directly.

## Customisation

- Add more endpoints to `src/app.py` and corresponding test cases to `tests/test_api.py`.
- Replace FastAPI with any ASGI/WSGI framework — only the server startup in `conftest.py` changes.
- Add `--timeout` or `--print=hHB` flags to httpie calls in tests for more verbose CI output.
