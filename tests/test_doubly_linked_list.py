from linked_lists import LinkedList


class TestCases:
    def test_class_definition(self):
        """Defines class with head and tail attributes."""
        linked = LinkedList()
        assert linked.head is None
        assert linked.tail is None

    def test_set_head(self, linked_list_nodes):
        """Adds node to head of list. Increments length."""
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

    def test_insert_default(self, empty_node, doubly_linked_list):
        """Inserts node at head by default and increments length"""
        assert doubly_linked_list.length == 3

        node_to_insert = empty_node
        node_to_insert.value = 2

        # 2 <--> 10 <--> 5 <--> 9
        doubly_linked_list.insert(node_to_insert)

        assert doubly_linked_list.head.value == 2

    def test_insert_before(self, linked_list_nodes, empty_node, doubly_linked_list):
        """Inserts node before specified node"""

        node_to_insert = empty_node
        node_to_insert.value = 24

        # 10 <--> 5 <--> 24 <--> 9
        doubly_linked_list.insert(
            node_to_insert, linked_list_nodes[9], insert_type="before"
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
        doubly_linked_list.insert(
            node_to_insert, linked_list_nodes[10], insert_type="after"
        )

        assert doubly_linked_list.head.next.value == 18
        assert doubly_linked_list.head.next.prev.value == 10
        assert doubly_linked_list.head.next.next.value == 5
        assert doubly_linked_list.head.next.next.prev.value == 18

    def test_remove(self, linked_list_nodes, doubly_linked_list):
        """Removes node from list and decrements length"""
        assert doubly_linked_list.length == 3
        # 10 <--> 9
        doubly_linked_list.remove(linked_list_nodes[5])
        assert doubly_linked_list.head.next.value == 9
        assert doubly_linked_list.head.next.prev.value == 10
        assert doubly_linked_list.length == 2

    def test_remove_head(self, linked_list_nodes, doubly_linked_list):
        """Removes node from head"""
        # 5 <--> 9
        doubly_linked_list.remove(linked_list_nodes[10])
        assert doubly_linked_list.head.value == 5
        assert doubly_linked_list.head.prev is None
        assert doubly_linked_list.head.next.value == 9

    def test_remove_tail(self, linked_list_nodes, doubly_linked_list):
        """Removes node from tail"""
        # 10 <--> 5
        doubly_linked_list.remove(linked_list_nodes[9])
        assert doubly_linked_list.tail.value == 5
        assert doubly_linked_list.tail.next is None
        assert doubly_linked_list.tail.prev.value == 10

    def test_contains(self, linked_list_nodes, empty_node, doubly_linked_list):
        """Returns boolean indicating whether node is present in list"""
        assert doubly_linked_list.contains(18) is False

        node_to_insert = empty_node
        node_to_insert.value = 18

        doubly_linked_list.insert(
            node_to_insert, linked_list_nodes[10], insert_type="after"
        )

        assert doubly_linked_list.contains(18) is True
