import pytest
from solutions import (
    ListNode,
    GraphNode,
    Queue,
    Stack,
    AdjList as Graph,
    LinkedList as DoublyLinkedList,
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
def products():
    return [
        {
            "id": 1,
            "name": "Ergonomic Rubber Wallet",
            "price": 3.38,
            "vendor": "Walmart",
        },
        {
            "id": 2,
            "name": "Sleek Iron Shoes",
            "price": 93.64,
            "vendor": "Dollar General",
        },
        {
            "id": 3,
            "name": "Durable Cotton Plate",
            "price": 73.2,
            "vendor": "Dollar General",
        },
        {"id": 4, "name": "Fantastic Leather Hat", "price": 21.57, "vendor": "Target"},
        {
            "id": 5,
            "name": "Awesome Silk Shoes",
            "price": 23.15,
            "vendor": "Dollar General",
        },
        {"id": 6, "name": "Rustic Steel Bench", "price": 16.93, "vendor": "Walmart"},
        {"id": 7, "name": "Awesome Leather Car", "price": 33.42, "vendor": "Walmart"},
        {
            "id": 8,
            "name": "Incredible Wool Lamp",
            "price": 70.04,
            "vendor": "Dollar General",
        },
        {"id": 9, "name": "Heavy Duty Bronze Car", "price": 40.36, "vendor": "Amazon"},
        {
            "id": 10,
            "name": "Ergonomic Rubber Wallet",
            "price": 26.81,
            "vendor": "Amazon",
        },
        {
            "id": 11,
            "name": "Incredible Wool Bench",
            "price": 0.06,
            "vendor": "Dollar General",
        },
        {
            "id": 12,
            "name": "Incredible Leather Clock",
            "price": 51.48,
            "vendor": "Amazon",
        },
        {
            "id": 13,
            "name": "Mediocre Granite Keyboard",
            "price": 18.35,
            "vendor": "Walmart",
        },
        {"id": 14, "name": "Small Iron Keyboard", "price": 56.49, "vendor": "Target"},
        {
            "id": 15,
            "name": "Synergistic Copper Bag",
            "price": 37.82,
            "vendor": "Walmart",
        },
        {
            "id": 16,
            "name": "Practical Concrete Knife",
            "price": 64.38,
            "vendor": "Amazon",
        },
        {"id": 17, "name": "Small Silk Hat", "price": 93.26, "vendor": "Target"},
        {
            "id": 18,
            "name": "Gorgeous Cotton Plate",
            "price": 65.54,
            "vendor": "Dollar General",
        },
        {
            "id": 19,
            "name": "Practical Aluminum Coat",
            "price": 32.7,
            "vendor": "Dollar General",
        },
        {"id": 20, "name": "Mediocre Wooden Plate", "price": 11.17, "vendor": "Amazon"},
        {"id": 21, "name": "Durable Bronze Pants", "price": 28.1, "vendor": "Target"},
        {"id": 22, "name": "Awesome Cotton Watch", "price": 71.32, "vendor": "Amazon"},
        {"id": 23, "name": "Fantastic Marble Chair", "price": 80.4, "vendor": "Target"},
        {
            "id": 24,
            "name": "Lightweight Bronze Watch",
            "price": 29.48,
            "vendor": "Walmart",
        },
        {
            "id": 25,
            "name": "Heavy Duty Concrete Watch",
            "price": 90.77,
            "vendor": "Target",
        },
        {"id": 26, "name": "Awesome Wooden Knife", "price": 77.4, "vendor": "Walmart"},
        {"id": 27, "name": "Awesome Wooden Chair", "price": 25.78, "vendor": "Target"},
        {
            "id": 28,
            "name": "Gorgeous Copper Clock",
            "price": 65.03,
            "vendor": "Dollar General",
        },
        {
            "id": 29,
            "name": "Practical Granite Clock",
            "price": 89.98,
            "vendor": "Dollar General",
        },
        {
            "id": 30,
            "name": "Fantastic Granite Keyboard",
            "price": 69.09,
            "vendor": "Dollar General",
        },
        {
            "id": 31,
            "name": "Ergonomic Cotton Keyboard",
            "price": 58.35,
            "vendor": "Amazon",
        },
        {
            "id": 32,
            "name": "Enormous Concrete Lamp",
            "price": 47.21,
            "vendor": "Amazon",
        },
        {
            "id": 33,
            "name": "Mediocre Plastic Hat",
            "price": 19.8,
            "vendor": "Dollar General",
        },
        {
            "id": 34,
            "name": "Enormous Concrete Coat",
            "price": 57.62,
            "vendor": "Walmart",
        },
        {"id": 35, "name": "Rustic Aluminum Pants", "price": 94.88, "vendor": "Target"},
        {
            "id": 36,
            "name": "Lightweight Linen Shirt",
            "price": 6.89,
            "vendor": "Dollar General",
        },
        {
            "id": 37,
            "name": "Heavy Duty Leather Pants",
            "price": 38.53,
            "vendor": "Target",
        },
        {
            "id": 38,
            "name": "Ergonomic Concrete Gloves",
            "price": 92.94,
            "vendor": "Walmart",
        },
        {
            "id": 39,
            "name": "Aerodynamic Paper Shoes",
            "price": 41.11,
            "vendor": "Dollar General",
        },
        {"id": 40, "name": "Rustic Paper Bag", "price": 95.87, "vendor": "Amazon"},
        {"id": 41, "name": "Awesome Linen Computer", "price": 8.74, "vendor": "Target"},
        {
            "id": 42,
            "name": "Mediocre Rubber Keyboard",
            "price": 86.52,
            "vendor": "Amazon",
        },
        {
            "id": 43,
            "name": "Enormous Rubber Gloves",
            "price": 31.67,
            "vendor": "Amazon",
        },
        {"id": 44, "name": "Mediocre Marble Knife", "price": 65.78, "vendor": "Target"},
        {
            "id": 45,
            "name": "Lightweight Wool Keyboard",
            "price": 33.67,
            "vendor": "Target",
        },
        {
            "id": 46,
            "name": "Heavy Duty Aluminum Pants",
            "price": 84.22,
            "vendor": "Target",
        },
        {
            "id": 47,
            "name": "Heavy Duty Cotton Gloves",
            "price": 95.02,
            "vendor": "Dollar General",
        },
        {
            "id": 48,
            "name": "Synergistic Bronze Lamp",
            "price": 33.52,
            "vendor": "Amazon",
        },
        {
            "id": 49,
            "name": "Lightweight Marble Knife",
            "price": 34.62,
            "vendor": "Amazon",
        },
        {"id": 50, "name": "Small Copper Clock", "price": 30.57, "vendor": "Target"},
        {"id": 51, "name": "Rustic Marble Car", "price": 85.27, "vendor": "Target"},
        {
            "id": 52,
            "name": "Incredible Copper Clock",
            "price": 37.89,
            "vendor": "Amazon",
        },
        {"id": 53, "name": "Enormous Aluminum Bag", "price": 87.31, "vendor": "Target"},
        {"id": 54, "name": "Fantastic Iron Watch", "price": 27.48, "vendor": "Walmart"},
        {"id": 55, "name": "Rustic Silk Keyboard", "price": 45.93, "vendor": "Walmart"},
        {
            "id": 56,
            "name": "Heavy Duty Rubber Chair",
            "price": 97.15,
            "vendor": "Walmart",
        },
        {
            "id": 57,
            "name": "Fantastic Leather Gloves",
            "price": 38.23,
            "vendor": "Amazon",
        },
        {
            "id": 58,
            "name": "Fantastic Steel Computer",
            "price": 39.5,
            "vendor": "Amazon",
        },
        {
            "id": 59,
            "name": "Heavy Duty Rubber Clock",
            "price": 98.18,
            "vendor": "Target",
        },
        {
            "id": 60,
            "name": "Aerodynamic Granite Plate",
            "price": 1.78,
            "vendor": "Target",
        },
        {
            "id": 61,
            "name": "Synergistic Wool Plate",
            "price": 71.47,
            "vendor": "Amazon",
        },
        {
            "id": 62,
            "name": "Synergistic Wooden Bench",
            "price": 99.63,
            "vendor": "Amazon",
        },
        {"id": 63, "name": "Fantastic Bronze Lamp", "price": 76.71, "vendor": "Amazon"},
        {
            "id": 64,
            "name": "Sleek Steel Chair",
            "price": 7.38,
            "vendor": "Dollar General",
        },
        {
            "id": 65,
            "name": "Ergonomic Marble Keyboard",
            "price": 74.58,
            "vendor": "Amazon",
        },
        {
            "id": 66,
            "name": "Synergistic Linen Shirt",
            "price": 25.85,
            "vendor": "Target",
        },
        {
            "id": 67,
            "name": "Mediocre Plastic Knife",
            "price": 82.99,
            "vendor": "Dollar General",
        },
        {"id": 68, "name": "Mediocre Plastic Watch", "price": 44.9, "vendor": "Target"},
        {"id": 69, "name": "Small Rubber Shirt", "price": 4.29, "vendor": "Walmart"},
        {"id": 70, "name": "Rustic Silk Clock", "price": 35.69, "vendor": "Walmart"},
        {
            "id": 71,
            "name": "Intelligent Plastic Keyboard",
            "price": 21.64,
            "vendor": "Target",
        },
        {
            "id": 72,
            "name": "Practical Iron Pants",
            "price": 37.94,
            "vendor": "Dollar General",
        },
        {"id": 73, "name": "Small Copper Bag", "price": 58.66, "vendor": "Amazon"},
        {
            "id": 74,
            "name": "Sleek Leather Plate",
            "price": 40.6,
            "vendor": "Dollar General",
        },
        {
            "id": 75,
            "name": "Intelligent Silk Chair",
            "price": 69.16,
            "vendor": "Target",
        },
        {
            "id": 76,
            "name": "Incredible Granite Coat",
            "price": 41.19,
            "vendor": "Target",
        },
        {
            "id": 77,
            "name": "Mediocre Concrete Bottle",
            "price": 74.21,
            "vendor": "Target",
        },
        {
            "id": 78,
            "name": "Synergistic Marble Chair",
            "price": 11.16,
            "vendor": "Walmart",
        },
        {"id": 79, "name": "Durable Linen Shirt", "price": 32.32, "vendor": "Walmart"},
        {"id": 80, "name": "Rustic Aluminum Bench", "price": 54.5, "vendor": "Target"},
        {
            "id": 81,
            "name": "Sleek Marble Watch",
            "price": 11.41,
            "vendor": "Dollar General",
        },
        {"id": 82, "name": "Ergonomic Iron Gloves", "price": 30.54, "vendor": "Amazon"},
        {
            "id": 83,
            "name": "Durable Concrete Plate",
            "price": 25.15,
            "vendor": "Dollar General",
        },
        {
            "id": 84,
            "name": "Rustic Rubber Keyboard",
            "price": 60.89,
            "vendor": "Amazon",
        },
        {
            "id": 85,
            "name": "Heavy Duty Cotton Shirt",
            "price": 54.51,
            "vendor": "Walmart",
        },
        {"id": 86, "name": "Awesome Silk Bag", "price": 62.47, "vendor": "Target"},
        {
            "id": 87,
            "name": "Lightweight Leather Computer",
            "price": 34.33,
            "vendor": "Walmart",
        },
        {"id": 88, "name": "Rustic Aluminum Shirt", "price": 26.84, "vendor": "Amazon"},
        {"id": 89, "name": "Aerodynamic Wool Hat", "price": 18.64, "vendor": "Target"},
        {
            "id": 90,
            "name": "Durable Marble Bottle",
            "price": 37.21,
            "vendor": "Dollar General",
        },
        {
            "id": 91,
            "name": "Intelligent Plastic Clock",
            "price": 16.28,
            "vendor": "Dollar General",
        },
        {
            "id": 92,
            "name": "Synergistic Leather Coat",
            "price": 26.62,
            "vendor": "Dollar General",
        },
        {
            "id": 93,
            "name": "Mediocre Wooden Gloves",
            "price": 20.91,
            "vendor": "Walmart",
        },
        {"id": 94, "name": "Enormous Bronze Clock", "price": 36.99, "vendor": "Amazon"},
        {
            "id": 95,
            "name": "Fantastic Marble Bottle",
            "price": 64.35,
            "vendor": "Walmart",
        },
        {"id": 96, "name": "Enormous Cotton Shoes", "price": 89.77, "vendor": "Target"},
        {
            "id": 97,
            "name": "Enormous Rubber Clock",
            "price": 18.0,
            "vendor": "Dollar General",
        },
        {"id": 98, "name": "Durable Silk Hat", "price": 31.6, "vendor": "Target"},
        {"id": 99, "name": "Gorgeous Concrete Car", "price": 72.7, "vendor": "Amazon"},
        {
            "id": 100,
            "name": "Ergonomic Wooden Keyboard",
            "price": 73.52,
            "vendor": "Dollar General",
        },
        {
            "id": 101,
            "name": "Ergonomic Cotton Watch",
            "price": 28.67,
            "vendor": "Walmart",
        },
        {"id": 102, "name": "Rustic Marble Car", "price": 26.03, "vendor": "Amazon"},
        {"id": 103, "name": "Mediocre Steel Bench", "price": 2.95, "vendor": "Target"},
        {
            "id": 104,
            "name": "Mediocre Paper Gloves",
            "price": 87.61,
            "vendor": "Walmart",
        },
        {
            "id": 105,
            "name": "Fantastic Steel Bottle",
            "price": 30.16,
            "vendor": "Amazon",
        },
        {
            "id": 106,
            "name": "Ergonomic Marble Watch",
            "price": 52.94,
            "vendor": "Target",
        },
        {
            "id": 107,
            "name": "Rustic Concrete Table",
            "price": 94.86,
            "vendor": "Dollar General",
        },
        {
            "id": 108,
            "name": "Mediocre Wool Computer",
            "price": 12.16,
            "vendor": "Amazon",
        },
        {
            "id": 109,
            "name": "Enormous Wooden Knife",
            "price": 77.63,
            "vendor": "Dollar General",
        },
        {"id": 110, "name": "Small Wooden Lamp", "price": 72.51, "vendor": "Amazon"},
        {
            "id": 111,
            "name": "Incredible Leather Shirt",
            "price": 11.32,
            "vendor": "Dollar General",
        },
        {
            "id": 112,
            "name": "Gorgeous Granite Chair",
            "price": 41.78,
            "vendor": "Dollar General",
        },
        {
            "id": 113,
            "name": "Incredible Aluminum Gloves",
            "price": 54.19,
            "vendor": "Walmart",
        },
        {"id": 114, "name": "Incredible Wool Coat", "price": 91.83, "vendor": "Target"},
        {
            "id": 115,
            "name": "Lightweight Granite Shoes",
            "price": 26.53,
            "vendor": "Walmart",
        },
        {
            "id": 116,
            "name": "Synergistic Paper Bench",
            "price": 86.51,
            "vendor": "Dollar General",
        },
        {
            "id": 117,
            "name": "Fantastic Cotton Computer",
            "price": 21.0,
            "vendor": "Target",
        },
        {
            "id": 118,
            "name": "Intelligent Cotton Pants",
            "price": 81.38,
            "vendor": "Amazon",
        },
        {
            "id": 119,
            "name": "Fantastic Leather Knife",
            "price": 59.29,
            "vendor": "Amazon",
        },
        {
            "id": 120,
            "name": "Heavy Duty Marble Chair",
            "price": 64.25,
            "vendor": "Amazon",
        },
        {
            "id": 121,
            "name": "Synergistic Steel Wallet",
            "price": 46.7,
            "vendor": "Walmart",
        },
        {
            "id": 122,
            "name": "Intelligent Plastic Car",
            "price": 88.78,
            "vendor": "Amazon",
        },
        {
            "id": 123,
            "name": "Intelligent Plastic Bench",
            "price": 19.41,
            "vendor": "Dollar General",
        },
        {
            "id": 124,
            "name": "Intelligent Copper Watch",
            "price": 82.6,
            "vendor": "Dollar General",
        },
        {"id": 125, "name": "Sleek Marble Hat", "price": 14.72, "vendor": "Walmart"},
        {
            "id": 126,
            "name": "Rustic Aluminum Bottle",
            "price": 56.72,
            "vendor": "Walmart",
        },
        {"id": 127, "name": "Gorgeous Leather Hat", "price": 77.86, "vendor": "Target"},
        {
            "id": 128,
            "name": "Lightweight Copper Shoes",
            "price": 60.31,
            "vendor": "Dollar General",
        },
    ]


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
