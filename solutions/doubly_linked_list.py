class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        prev_head = self.head
        self.head = node

        if prev_head:
            prev_head.prev = self.head
            self.head.next = prev_head

    def set_tail(self, node):
        prev_tail = self.tail
        self.tail = node

        if prev_tail:
            prev_tail.next = self.tail
            self.tail.prev = prev_tail

    def insert_before(self, node, insert_node):
        curr = self.head

        while curr != None:
            if curr.value == node.value:
                insert_node.prev = curr.prev
                insert_node.next = curr

                curr.prev = insert_node
                break

            curr = curr.next
