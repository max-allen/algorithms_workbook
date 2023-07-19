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


def bfs(graph, src, dest):
    queue = deque()
    queue.append(src)

    while len(queue):
        curr = queue.popleft()
        if curr == dest:
            return True

        for edge in graph[curr]:
            queue.append(edge)

    return False


def dfs(graph, vertex, target):
    if vertex == target:
        return True

    for edge in graph[vertex]:
        return dfs(graph, edge, target)

    return False


def check_path_exists(src, dest, paths):
    adj_list = defaultdict(list)
    for path in paths:
        for key in path:
            adj_list[key].append(path[key])

    return bfs(adj_list, src, dest)
