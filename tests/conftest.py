import pytest

from graphs import GraphNode, AdjList as Graph
from linked_lists import (
    build_list_from_values,
    ListNode,
    LinkedList as DoublyLinkedList,
)

from solutions import (
    Queue,
    Stack,
)


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
def two_sum_match():
    return [{"arr": [2, 7, 11, 15], "target": 9}, {"arr": [3, 2, 4], "target": 6}]


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


@pytest.fixture
def paths():
    return [
        {"foo": "bar"},
        {"bar": "baz"},
        {"qux": "quux"},
        {"corge": "grault"},
        {"garply": "waldo"},
        {"fred": "plugh"},
        {"xyzzy": "thud"},
    ]


@pytest.fixture
def filesystem_paths():
    paths = [
        "account/settings",
        "account/settings/activity/client/home",
        "profile/activity/team/client",
        "account/notifications",
        "about/contact/name",
        "about",
        "home",
        "about/team",
        "about/address",
    ]

    return {
        "string": "\n".join(paths),
        "hash": {
            "account": {
                "settings": {"activity": {"client": {"home": {}}}},
                "notifications": {},
            },
            "profile": {"activity": {"team": {"client": {}}}},
            "about": {
                "contact": {"name": {}},
                "team": {},
                "address": {},
            },
            "home": {},
        },
    }


@pytest.fixture
def graph():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "D")
    g.add_edge("B", "E")
    g.add_edge("B", "F")
    g.add_edge("C")
    g.add_edge("D", "G")
    g.add_edge("D", "H")
    g.add_edge("E")
    g.add_edge("F", "I")
    g.add_edge("F", "J")
    g.add_edge("G", "K")
    g.add_edge("H")
    g.add_edge("I")
    g.add_edge("J")
    g.add_edge("K")

    return {
        "fixture": g,
        "dfs_a_expected": ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"],
        "bfs_a_expected": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
    }


@pytest.fixture
def is_mountain_peak_lists():
    return [[1, 2, 3, 4, 3, 2, 1], [1, 2, 1, 4, 3, 2, 1], [1, 2, 3, 4, 3, 4, 1]]


@pytest.fixture
def flood_fill_color_change():
    return {
        "input": [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        "start_row": 1,
        "start_col": 1,
        "color": 2,
        "expected": [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    }


@pytest.fixture
def flood_fill_no_connection():
    return {
        "input": [[0, 0, 0], [0, 0, 0]],
        "start_row": 0,
        "start_col": 0,
        "color": 0,
        "expected": [[0, 0, 0], [0, 0, 0]],
    }


@pytest.fixture
def river_sizes_matrix():
    return {
        "matrix": [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ],
        "expected": [2, 1, 5, 2, 2],
    }


@pytest.fixture
def graph_nodes():
    n1 = GraphNode(1)
    n2 = GraphNode(2, [n1])
    n3 = GraphNode(3, [n2])

    return {"n1": n1, "n2": n2, "n3": n3}


@pytest.fixture
def integer_lists():
    return {
        "unsorted": [10, 9, 7, 15, 11, 2, 5, 6],
        "sorted": [2, 5, 6, 7, 9, 10, 11, 15],
    }


@pytest.fixture
def non_overlapping_ranges():
    return [[2, 4], [4, 6]]


@pytest.fixture
def parentheses_inputs():
    return [("()", True), ("()[]{}", True), ("(]", False), ("(){", False)]


@pytest.fixture
def parentheses_repeating_input():
    return "((({{{}}})))"


@pytest.fixture
def sorted_lists_merged():
    return {
        "list_one": build_list_from_values([1, 2, 4]),
        "list_two": build_list_from_values([1, 3, 4]),
        "expected": [1, 1, 2, 3, 4, 4],
    }


@pytest.fixture
def sorted_intervals():
    return [
        {
            "existing_intervals": [[1, 3], [6, 9]],
            "insert_interval": [2, 5],
            "expected": [[1, 5], [6, 9]],
        },
        {
            "existing_intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            "insert_interval": [4, 8],
            "expected": [[1, 2], [3, 10], [12, 16]],
        },
    ]
