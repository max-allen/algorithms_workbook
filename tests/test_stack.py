from solutions import Stack


class TestCases:
    def test_push(self):
        """Inserts item at the front of the stack"""
        stack = Stack()

        stack.push("foo")
        stack.push("bar")
        stack.push("baz")

        assert stack.items.length == 3
        assert stack.items.head.value == "baz"

    def test_pop(self, stack):
        """Returns and removes item at the front of the stack"""
        assert stack.items.head.value == "baz"
        popped = stack.pop()
        assert popped == "baz"
