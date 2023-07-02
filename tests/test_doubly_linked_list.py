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

    def test_insert_before(self, linked_list_nodes, empty_node, doubly_linked_list):
        """Inserts node before specified node"""

        node_to_insert = empty_node
        node_to_insert.value = 24

        # 10 <--> 5 <--> 24 <--> 9
        doubly_linked_list.insert(
            linked_list_nodes[9], node_to_insert, insert_type="before"
        )

        assert doubly_linked_list.head.next.next.value == 24
        assert doubly_linked_list.head.next.next.prev.value == 5
        assert doubly_linked_list.head.next.next.next.value == 9
        assert doubly_linked_list.head.next.next.next.prev.value == 24

    def test_insert_after(self, linked_list_nodes, empty_node, doubly_linked_list):
        """Inserts node after specified node by default"""

        node_to_insert = empty_node
        node_to_insert.value = 18

        # 10 <--> 18 <--> 5 <--> 9
        doubly_linked_list.insert(linked_list_nodes[10], node_to_insert)

        assert doubly_linked_list.head.next.value == 18
        assert doubly_linked_list.head.next.prev.value == 10
        assert doubly_linked_list.head.next.next.value == 5
        assert doubly_linked_list.head.next.next.prev.value == 18
