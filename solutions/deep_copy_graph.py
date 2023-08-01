from .helpers import GraphNode as Node
from collections import deque


def dfs(node, visited):
    if node in visited:
        return visited[node]

    copy = Node(node.value)
    visited[node] = copy

    for neighbor in node.neighbors:
        copy.neighbors.append(dfs(neighbor, visited))

    return copy


def bfs(node):
    # process node and neighbors
    # enqueue processing of neighbors neighbors
    visited = {}
    queue = deque()
    queue.append(node)

    visited[node] = Node(node.value)

    while len(queue):
        curr = queue.popleft()
        copy = visited[curr]

        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.value)
                queue.append(neighbor)

            copy.neighbors.append(visited[neighbor])

    return visited[node]


def deep_copy(node):
    return bfs(node)


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
