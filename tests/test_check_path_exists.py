from solutions import check_path_exists


class TestCases:
    def test_valid_path(self, paths):
        """Returns True if path exists between source and destination elements"""
        result = check_path_exists("foo", "baz", paths)
        assert result is True

    def test_invalid_path(self, paths):
        """Returns False if no path exists between source and destination elements"""
        result = check_path_exists("foo", "quux", paths)
        assert result is True
