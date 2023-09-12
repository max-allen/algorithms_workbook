# Write a program that retruns the middle node. If list
# has even length, return second middle node.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_middle_node(linked_list):
    counter = 0
    curr = linked_list

    while curr:
        counter += 1
        curr = curr.next

    middle_index = counter // 2
    middle_node = linked_list

    while middle_index:
        middle_index -= 1
        middle_node = middle_node.next

    return middle_node
