from solutions import Queue


class TestCases:
    def test_enqueue(self):
        """Inserts item at the back of the queue"""
        queue = Queue()

        queue.enqueue("foo")
        queue.enqueue("bar")
        queue.enqueue("baz")

        assert queue.items.length == 3
        assert queue.items.tail.value == "foo"

    def test_dequeue(self, queue):
        """Returns and removes item at the front of the queue"""
        assert queue.items.tail.value == "foo"
        dequeued = queue.dequeue()
        assert dequeued == "foo"
