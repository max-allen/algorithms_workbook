from solutions import can_schedule


class TestCases:
    def test_non_overlapping(self, non_overlapping_ranges):
        assert can_schedule(non_overlapping_ranges, [0, 1]) is True
        assert can_schedule(non_overlapping_ranges, [7, 8]) is True

    def test_overlapping(self, non_overlapping_ranges):
        assert can_schedule(non_overlapping_ranges, [1, 3]) is False
        assert can_schedule(non_overlapping_ranges, [5, 6]) is False
