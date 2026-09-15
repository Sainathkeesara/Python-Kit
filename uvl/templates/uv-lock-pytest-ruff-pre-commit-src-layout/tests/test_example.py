# last_verified: 2026-09-15
"""Example tests demonstrating pytest features with the package."""

from __future__ import annotations

import pytest
from mypackage import __version__


class TestPackageMetadata:
    """Tests for package metadata."""

    def test_version_format(self):
        """Version follows semantic versioning."""
        parts = __version__.split(".")
        assert len(parts) == 3
        assert all(part.isdigit() for part in parts)

    def test_version_not_empty(self):
        """Version is not empty."""
        assert __version__


class TestExample:
    """Example unit tests."""

    def test_sample_data_fixture(self, sample_data: dict[str, str]):
        """Test that sample_data fixture works."""
        assert sample_data["key"] == "value"
        assert sample_data["number"] == "42"

    def test_temp_file_fixture(self, temp_file):
        """Test that temp_file fixture works."""
        assert temp_file.exists()
        assert temp_file.read_text() == "test content"

    @pytest.mark.parametrize(
        "input_val,expected",
        [
            (1, 2),
            (2, 3),
            (10, 11),
        ],
    )
    def test_parametrized_increment(self, input_val: int, expected: int):
        """Test parametrized increment function."""
        assert input_val + 1 == expected

    @pytest.mark.slow
    def test_slow_marker(self):
        """Test marked as slow."""
        import time

        time.sleep(0.01)
        assert True

    @pytest.mark.integration
    def test_integration_marker(self):
        """Test marked as integration."""
        assert True