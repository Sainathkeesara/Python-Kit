# last_verified: 2026-09-15
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