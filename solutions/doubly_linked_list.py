class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def set_head(self, node):
        prev_head = self.head
        self.head = node

        if prev_head:
            prev_head.prev = self.head
            self.head.next = prev_head

        if self.tail and self.tail.prev is None:
            self.tail.prev = self.head
            self.head.next = self.tail

        self.increment_length()

    def set_tail(self, node):
        prev_tail = self.tail
        self.tail = node

        if prev_tail:
            prev_tail.next = self.tail
            self.tail.prev = prev_tail

        if self.head and self.head.next is None:
            self.head.next = self.tail
            self.tail.prev = self.head

        self.increment_length()

    def insert(self, node, insert_node, insert_type="after"):
        curr = self.head

        while curr is not None:
            if curr.value == node.value:
                if insert_type == "before":
                    insert_node.prev = curr.prev
                    insert_node.next = curr

                    curr.prev.next = insert_node
                    curr.prev = insert_node
                    break
                else:
                    insert_node.prev = curr
                    insert_node.next = curr.next

                    curr.next.prev = insert_node
                    curr.next = insert_node
                    break
            curr = curr.next

        self.increment_length()

    def increment_length(self):
        self.length += 1
