from solutions import insertion_sort


class TestCases:
    def test_sort_result(self, integer_lists):
        assert insertion_sort(integer_lists["unsorted"]) == integer_lists["sorted"]
