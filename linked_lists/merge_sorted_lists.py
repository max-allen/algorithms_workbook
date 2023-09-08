from .utils import SinglyLinked as ListNode


def merge_sorted_lists(list_one, list_two):
    curr = merged = ListNode()

    while list_one and list_two:
        if list_one.value < list_two.value:
            curr.next = ListNode(list_one.value)
            list_one = list_one.next
        else:
            curr.next = ListNode(list_two.value)
            list_two = list_two.next

        curr = curr.next

    if list_one or list_two:
        node = list_one if list_one else list_two

        while node:
            curr.next = ListNode(node.value)
            node = node.next

    return merged.next
