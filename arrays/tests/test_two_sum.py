from arrays import two_sum


class TestCases:
    def test_match(self, two_sum_match):
        result = two_sum(two_sum_match[0]["arr"], two_sum_match[0]["target"])
        assert result == [0, 1] or result == [1, 0]

        result = two_sum(two_sum_match[1]["arr"], two_sum_match[1]["target"])
        assert result == [1, 2] or result == [2, 1]
