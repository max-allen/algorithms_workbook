from collections import defaultdict, deque


class AdjList:
    def __init__(self):
        self.vertices = defaultdict(list)

    def add_edge(self, u, v=None):
        if v is not None:
            self.vertices[u].append(v)
        else:
            self.vertices[u]

    def depth_first_search(self, vertex, arr=[]):
        arr.append(vertex)

        for edge in self.vertices[vertex]:
            self.depth_first_search(edge, arr)

        return arr

    def breadth_first_search(self, vertex):
        arr = []
        queue = deque()
        queue.append(vertex)

        while len(queue):
            curr = queue.popleft()
            arr.append(curr)
            for edge in self.vertices[curr]:
                queue.append(edge)

        return arr
