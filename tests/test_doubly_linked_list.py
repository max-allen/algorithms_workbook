from solutions import LinkedList, Node


class TestCases:
    def test_class_definition(self):
        """Defines class with head and tail attributes."""
        linked = LinkedList()
        assert linked.head is None
        assert linked.tail is None

    def test_set_head(self):
        """Adds node to head of list"""
        linked = LinkedList()

        linked.set_head(Node(5))
        linked.set_head(Node(10))
        linked.set_head(Node(3))

        assert linked.head.value == 3
        assert linked.head.next.value == 10
        assert linked.head.next.next.value == 5

    def test_set_tail(self):
        """Adds node to end of list"""
        linked = LinkedList()

        linked.set_tail(Node(1))
        linked.set_tail(Node(9))
        linked.set_tail(Node(4))

        assert linked.tail.value == 4
        assert linked.tail.prev.value == 9
        assert linked.tail.prev.prev.value == 1
