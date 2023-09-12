import pytest

from linked_lists import (
    build_list_from_values,
    ListNode,
    LinkedList as DoublyLinkedList,
)


class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next = None


@pytest.fixture
def linked_list_nodes():
    return {
        5: ListNode(5),
        10: ListNode(10),
        3: ListNode(3),
        1: ListNode(1),
        9: ListNode(9),
        4: ListNode(4),
        12: ListNode(12),
    }


@pytest.fixture
def singly_linked_list(linked_list_nodes):
    linked_list = LinkedList(linked_list_nodes[4].value)
    linked_list.next = linked_list_nodes[9]
    linked_list.next.next = linked_list_nodes[9]
    linked_list.next.next.next = linked_list_nodes[10]
    return linked_list


@pytest.fixture
def odd_length_linked_list(singly_linked_list, linked_list_nodes):
    linked_list = singly_linked_list
    while linked_list != linked_list_nodes[10]:
        linked_list = linked_list.next

    linked_list.next = linked_list_nodes[1]
    linked_list.next.next = linked_list_nodes[3]
    linked_list.next.next.next = linked_list_nodes[5]
    linked_list.next.next.next.next = linked_list_nodes[12]
    return singly_linked_list


@pytest.fixture
def doubly_linked_list(linked_list_nodes):
    linked_list = DoublyLinkedList()

    # 10 <--> 5 <--> 9

    linked_list.set_head(linked_list_nodes[5])
    linked_list.set_tail(linked_list_nodes[9])
    linked_list.set_head(linked_list_nodes[10])
    return linked_list


@pytest.fixture
def empty_node():
    return ListNode()


@pytest.fixture
def linked_list_sum_prompt():
    linked_list_one = DoublyLinkedList()
    linked_list_two = DoublyLinkedList()
    linked_list_three = DoublyLinkedList()

    list_one_elements = [1, 7, 4, 2]
    list_two_elements = [5, 4, 9]
    list_three_elements = [2, 2, 9, 1]

    for el in list_one_elements:
        linked_list_one.insert(ListNode(el))

    for el in list_two_elements:
        linked_list_two.insert(ListNode(el))

    for el in list_three_elements:
        empty_node.value = el
        linked_list_three.insert(ListNode(el))

    return {
        "list_one": linked_list_one,
        "list_two": linked_list_two,
        "expected": linked_list_three,
    }


@pytest.fixture
def sorted_lists_merged():
    return {
        "list_one": build_list_from_values([1, 2, 4]),
        "list_two": build_list_from_values([1, 3, 4]),
        "expected": [1, 1, 2, 3, 4, 4],
    }
