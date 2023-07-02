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

        self.update_length()

    def set_tail(self, node):
        prev_tail = self.tail
        self.tail = node

        if prev_tail:
            prev_tail.next = self.tail
            self.tail.prev = prev_tail

        if self.head and self.head.next is None:
            self.head.next = self.tail
            self.tail.prev = self.head

        self.update_length()

    def insert(self, insert_node, find_node=None, insert_type=None):
        curr = self.head

        if find_node is None and insert_type is None:
            self.set_head(insert_node)
        else:
            while curr is not None:
                if curr.value == find_node.value:
                    if insert_type == "before":
                        insert_node.prev = curr.prev
                        insert_node.next = curr

                        curr.prev.next = insert_node
                        curr.prev = insert_node
                        break
                    elif insert_type == "after":
                        insert_node.prev = curr
                        insert_node.next = curr.next

                        curr.next.prev = insert_node
                        curr.next = insert_node
                        break
                curr = curr.next

        self.update_length()

    def remove(self, remove_node):
        curr = self.head

        while curr is not None:
            if curr.value == remove_node.value:
                if curr == self.head and self.head.next:
                    self.head = self.head.next
                    self.head.prev = None
                    self.head.next.prev = self.head

                elif curr == self.tail and self.tail.prev:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    self.tail.prev.next = None

                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev

                curr = None
                break

            curr = curr.next

        self.update_length("dec")

    def update_length(self, operation_type="inc"):
        self.length = self.length + 1 if operation_type == "inc" else self.length - 1
