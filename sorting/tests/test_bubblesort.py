from sorting import bubble_sort


class TestClass:
    def test_sort_result(self, integer_lists):
        assert bubble_sort(integer_lists["unsorted"]) == integer_lists["sorted"]
