from linked_lists import ListNode as Node, LinkedList


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, value):
        node = Node(value)
        self.items.insert(node)

    def dequeue(self):
        dequeued = self.items.remove(self.items.tail)
        return dequeued
