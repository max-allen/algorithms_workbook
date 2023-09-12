from strings import is_subsequence


class TestCases:
    def test_valid(self, is_subsequence_valid):
        """Returns true for valid cases"""
        result = is_subsequence(
            is_subsequence_valid["arr"], is_subsequence_valid["sequence"]
        )
        assert result is True

    def test_invalid_duplicate(self, is_subsequence_invalid_duplicate):
        """Returns false when repeating element is not contained by array"""
        result = is_subsequence(
            is_subsequence_invalid_duplicate["arr"],
            is_subsequence_invalid_duplicate["sequence"],
        )
        assert result is False

    def test_invalid_non_members(self, is_subsequence_invalid_non_members):
        """Returns false when repeating element is not contained by array"""
        result = is_subsequence(
            is_subsequence_invalid_non_members["arr"],
            is_subsequence_invalid_non_members["sequence"],
        )
        assert result is False
