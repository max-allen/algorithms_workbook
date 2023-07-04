from .doubly_linked_list import LinkedList
from .helpers import Node

# Given a list of objects where each key value pair indicates a path between two elements,
# deterimine whether a vaild path exists between the specified source and destination elements.

# [
#     {"foo": "bar"},
#     {"bar": "baz"},
#     {"qux": "quux"},
#     {"corge": "grault"},
#     {"garply": "waldo"},
#     {"fred": "plugh"},
#     {"xyzzy": "thud"},
# ]

# foo, bar -> true
# foo, baz -> true
# foo, quux -> false


def check_path_exists(src, dest, paths):
    linked = LinkedList()

    for path in paths:
        for key in path:
            value = path[key]

            linked.insert(Node(key))
            linked.insert(Node(value))

    src_node = linked.find_by_value(src)

    if src_node is None:
        return False

    curr = src_node

    while curr is not None:
        if curr.value == dest:
            return True
        curr = curr.next

    curr = src_node

    while curr is not None:
        if curr.value == dest:
            return True

        curr = curr.prev

    return False
