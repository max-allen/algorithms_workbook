import pytest
from solutions import Node, Queue, Stack, LinkedList as DoublyLinkedList


@pytest.fixture
def key_count_fixture():
    return {
        "foo": {"bar": {}},
        "baz": {
            "quux": {"corge": {"foo": {"corge": {}}}},
        },
        "quux": {},
        "corge": {},
    }


@pytest.fixture
def two_number_sum_match():
    return {"arr": [3, 5, -4, 8, 11, 1, -1, 6], "target": 10}


@pytest.fixture
def two_number_sum_no_match():
    return {"arr": [1, 0, 8, 11, 5, -1, 6], "target": 100}


@pytest.fixture
def three_number_sum_multiple():
    return {
        "arr": [12, 3, 1, 2, -6, 5, -8, 6],
        "target": 0,
        "expected": [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
    }


@pytest.fixture
def three_number_sum_single():
    return {
        "arr": [1, 2, 3],
        "target": 6,
        "expected": [[1, 2, 3]],
    }


@pytest.fixture
def three_number_sum_no_match(three_number_sum_multiple):
    return {"arr": three_number_sum_multiple["arr"], "target": 1000, "expected": []}


@pytest.fixture
def is_subsequence_valid():
    return {"arr": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10]}


@pytest.fixture
def is_subsequence_invalid_duplicate():
    return {"arr": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, -1]}


@pytest.fixture
def is_subsequence_invalid_non_members():
    return {
        "arr": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, 10, 11, 11, 11, 11],
    }


@pytest.fixture
def is_palindrome_valid():
    return "abcdcba"


@pytest.fixture
def is_palindrome_invalid():
    return "abcdefg"


@pytest.fixture
def is_palindrome_valid_spaces():
    return "Was it a car or a cat I saw"


@pytest.fixture
def get_nth_fibonacci_sequence():
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next = None


@pytest.fixture
def linked_list_nodes():
    return {5: Node(5), 10: Node(10), 3: Node(3), 1: Node(1), 9: Node(9), 4: Node(4)}


@pytest.fixture
def singly_linked_list(linked_list_nodes):
    linked_list = LinkedList(linked_list_nodes[4].value)
    linked_list.next = linked_list_nodes[9]
    linked_list.next.next = linked_list_nodes[9]
    linked_list.next.next.next = linked_list_nodes[10]
    return linked_list


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
    return Node()


@pytest.fixture
def queue():
    q = Queue()

    q.enqueue("foo")
    q.enqueue("bar")
    q.enqueue("baz")
    return q


@pytest.fixture
def stack():
    s = Stack()

    s.push("foo")
    s.push("bar")
    s.push("baz")
    return s
