from linked_lists import sum_linked_lists


class TestCases:
    def test_prompt(self, linked_list_sum_prompt):
        """Adds lists and returns correct result."""

        result = sum_linked_lists(
            linked_list_sum_prompt["list_one"], linked_list_sum_prompt["list_two"]
        )

        expected = linked_list_sum_prompt["expected"]

        assert result.head.value == expected.head.value
        assert result.head.next.value == expected.head.next.value
        assert result.head.next.next.value == expected.head.next.next.value
        assert result.head.next.next.next.value == expected.head.next.next.next.value
