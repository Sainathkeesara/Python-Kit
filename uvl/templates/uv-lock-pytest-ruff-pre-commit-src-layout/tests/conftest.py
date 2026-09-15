# last_verified: 2026-09-15 · uv 0.6.0, pytest 8.3.0, ruff 0.7.0, mypy 1.13.0, pre-commit 4.0.0
"""Shared pytest fixtures and configuration."""

from __future__ import annotations

import pytest


@pytest.fixture(scope="session")
def sample_data() -> dict[str, str]:
    """Provide sample data for tests."""
    return {"key": "value", "number": "42"}


@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    f = tmp_path / "temp.txt"
    f.write_text("test content")
    return f