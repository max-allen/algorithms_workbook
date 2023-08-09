from solutions import get_middle_node


class TestCases:
    def test_odd_length(self, odd_length_linked_list, linked_list_nodes):
        curr = odd_length_linked_list
        while curr:
            curr = curr.next

        middle_node = get_middle_node(odd_length_linked_list)
        assert middle_node == linked_list_nodes[1]
