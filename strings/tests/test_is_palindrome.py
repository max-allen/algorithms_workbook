from strings import is_palindrome


class TestCases:
    def test_valid(self, is_palindrome_valid):
        """Returns true for valid cases"""
        result = is_palindrome(is_palindrome_valid)
        assert result is True

    def test_invalid(self, is_palindrome_invalid):
        """Returns false for invalid cases"""
        result = is_palindrome(is_palindrome_invalid)
        assert result is False

    def test_valid_spaces(self, is_palindrome_valid_spaces):
        """Returns true for valid cases including spaces"""
        result = is_palindrome(is_palindrome_valid_spaces)
        assert result is False
