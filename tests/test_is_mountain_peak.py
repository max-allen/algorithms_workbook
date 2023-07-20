from solutions import is_mountain_peak


class TestCases:
    def test_valid_mountain_peak(self, is_mountain_peak_lists):
        assert is_mountain_peak(is_mountain_peak_lists[0]) is True

    def test_invalid_mountain_peak(self, is_mountain_peak_lists):
        assert is_mountain_peak(is_mountain_peak_lists[1]) is False
        assert is_mountain_peak(is_mountain_peak_lists[2]) is False
