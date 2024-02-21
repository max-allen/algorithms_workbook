from .utils import GraphNode as Node
from collections import deque


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


def deep_copy(node, visited={}):
    if node in visited:
        return visited[node]

    copy = Node(node.value)
    visited[node] = copy

    for neighbor in node.neighbors:
        copy.neighbors.append(deep_copy(neighbor, visited))

    return copy
