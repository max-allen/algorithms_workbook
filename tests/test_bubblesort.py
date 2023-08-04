from solutions import bubblesort


class TestClass:
    def test_sort_result(self, integer_lists):
        assert bubblesort(integer_lists["unsorted"]) == integer_lists["sorted"]
