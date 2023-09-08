class DoublyLinked:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class SinglyLinked:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_list_values(self):
        values = []
        curr = self

        while curr:
            values.append(curr.value)
            curr = curr.next

        return values


def build_list_from_values(values):
    list_node = SinglyLinked(values[0])
    curr = list_node

    for value in values[1:]:
        curr.next = SinglyLinked(value)
        curr = curr.next

    return list_node
