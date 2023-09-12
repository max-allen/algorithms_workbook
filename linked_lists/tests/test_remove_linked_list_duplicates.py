from linked_lists import remove_linked_list_duplicates


class TestCases:
    def test_return_value(self, singly_linked_list):
        """Returns the list with duplicate values removed"""
        deduped_list = remove_linked_list_duplicates(singly_linked_list)
        assert deduped_list.next.next.value == 10
