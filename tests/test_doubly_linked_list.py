from solutions import LinkedList


class TestCases:
    def test_class_definition(self):
        """Defines class with head and tail attributes."""
        linked = LinkedList()
        assert linked.head is None
        assert linked.tail is None

    def test_set_head(self, linked_list_nodes):
        """Adds node to head of list"""
        linked = LinkedList()

        linked.set_head(linked_list_nodes[5])
        linked.set_head(linked_list_nodes[10])
        linked.set_head(linked_list_nodes[3])

        assert linked.head.value == 3
        assert linked.head.next.value == 10
        assert linked.head.next.next.value == 5

    def test_set_tail(self, linked_list_nodes):
        """Adds node to end of list"""
        linked = LinkedList()

        linked.set_tail(linked_list_nodes[1])
        linked.set_tail(linked_list_nodes[9])
        linked.set_tail(linked_list_nodes[4])

        assert linked.tail.value == 4
        assert linked.tail.prev.value == 9
        assert linked.tail.prev.prev.value == 1
