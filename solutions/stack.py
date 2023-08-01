from . import ListNode as Node, LinkedList


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def push(self, value):
        node = Node(value)
        self.items.insert(node)

    def pop(self):
        popped = self.items.remove(self.items.head)
        return popped
