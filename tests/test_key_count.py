import pytest
from solutions import key_count


class TestKeyCount:
    def test_count_nested(self, key_count_fixture):
        """Should correctly count nested keys"""
        count = key_count(key_count_fixture, "bar")
        assert count == 1

    def test_count_root_and_nested(self, key_count_fixture):
        """Should correctly key nested and at object root"""
        count = key_count(key_count_fixture, "corge")
        assert count == 3

    def test_count_non_entry(self, key_count_fixture):
        """Should correctly count keys not on object"""
        count = key_count(key_count_fixture, "grault")
        assert count == 0
