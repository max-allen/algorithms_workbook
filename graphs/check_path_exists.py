from collections import defaultdict, deque

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
    graph = defaultdict(list)

    for path in paths:
        for key in path:
            graph[key].append(path[key])

    def dfs(vertex):
        if vertex == dest:
            return True

        for edge in graph[vertex]:
            return dfs(edge)

        return False

    return dfs(src)
