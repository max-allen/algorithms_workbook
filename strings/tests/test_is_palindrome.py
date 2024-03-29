from strings import is_palindrome


class TestCases:
    def test_valid_palindrome(self, is_palindrome_valid):
        """Returns true for valid cases"""
        result = is_palindrome(is_palindrome_valid)
        assert result is True

    def test_invalid_palindrome(self, is_palindrome_invalid):
        """Returns false for invalid cases"""
        result = is_palindrome(is_palindrome_invalid)
        assert result is False

    def test_valid_palindrome_spaces(self, is_palindrome_valid_spaces):
        """Returns true for valid cases including spaces"""
        result = is_palindrome(is_palindrome_valid_spaces)
        assert result is True

    def test_valid_palindrome_colon(self, is_palindrome_valid_colon):
        """Returns true for valid cases including punctuation"""
        result = is_palindrome(is_palindrome_valid_colon)
        assert result is True
