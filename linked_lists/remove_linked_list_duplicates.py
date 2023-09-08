def remove_linked_list_duplicates(linked_list):
    curr = linked_list

    while curr.next is not None:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return linked_list
