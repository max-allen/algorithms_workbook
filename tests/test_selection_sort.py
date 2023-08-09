from solutions import selection_sort


class TestClass:
    def test_sort_result(self, integer_lists):
        assert selection_sort(integer_lists["unsorted"]) == integer_lists["sorted"]
