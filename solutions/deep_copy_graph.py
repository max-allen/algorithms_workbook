from .helpers import GraphNode as Node


def dfs(node, visited):
    if node in visited:
        return visited[node]

    copy = Node(node.value)
    visited[node] = copy

    for neighbor in node.neighbors:
        copy.neighbors.append(dfs(neighbor, visited))

    return copy


def deep_copy(node):
    visited = {}
    return dfs(node, visited)


def test_deep_copy(orig, copy):
    if orig == copy:
        return False

    if orig.value != copy.value:
        return False

    if len(orig.neighbors) != len(copy.neighbors):
        return False

    for neighbor_idx in range(len(orig.neighbors)):
        next_one = orig.neighbors[neighbor_idx]
        next_two = copy.neighbors[neighbor_idx]
        return test_deep_copy(next_one, next_two)

    return True
