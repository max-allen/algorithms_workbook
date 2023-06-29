from solutions import three_number_sum


class TestCases:
    def test_single(self, three_number_sum_single):
        """Should return triplet correctly"""
        result = three_number_sum(
            three_number_sum_single["arr"],
            three_number_sum_single["target"],
        )
        assert result == three_number_sum_single["expected"]

    def test_multiple(self, three_number_sum_multiple):
        """Should return all results if there are multiple triplets"""
        result = three_number_sum(
            three_number_sum_multiple["arr"], three_number_sum_multiple["target"]
        )
        assert result == three_number_sum_multiple["expected"]

    def test_no_match(self, three_number_sum_no_match):
        """Should return empty list given no results"""
        result = three_number_sum(
            three_number_sum_no_match["arr"], three_number_sum_no_match["target"]
        )
        assert result == three_number_sum_no_match["expected"]
