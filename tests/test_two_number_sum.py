from solutions import two_number_sum


class TestCases:
    def test_match(self, two_number_sum_match):
        """Should return matching pairs"""
        result = two_number_sum(
            two_number_sum_match["arr"], two_number_sum_match["target"]
        )
        assert result == [-1, 11] or result == [11, -1]

    def test_no_match(self, two_number_sum_no_match):
        assert (
            two_number_sum(
                two_number_sum_no_match["arr"], two_number_sum_no_match["target"]
            )
            == []
        )
