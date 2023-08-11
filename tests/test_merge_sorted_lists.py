from solutions import merge_sorted_lists


class TestCases:
    def test_result(self, sorted_lists_merged):
        assert (
            merge_sorted_lists(
                sorted_lists_merged["list_one"],
                sorted_lists_merged["list_two"],
            ).get_list_values()
            == sorted_lists_merged["expected"]
        )
