from strings import is_valid_anagram


class TestCases:
    def test_is_valid_anagram(self, valid_anagram):
        first, second = valid_anagram
        assert is_valid_anagram(first, second) is True

    def test_invalid_anagram(self, invalid_anagram):
        first, second = invalid_anagram
        assert is_valid_anagram(first, second) is False
