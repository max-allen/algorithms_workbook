# Graphs

A graph is a structure containing a set of objects (nodes/vertices) and edges,
which indicate relationships between unordered object pairs.

Edges can be directed or undirected and can optionally have values
(weighted graphs). Trees are undirected graphs in which any two vertices are
connected by exactly one edge and there can be no cycles in the graph.

Graphs are commonly used to model relationships between unordered entities:

- **Social Media**: Each Facebook user can be represented as vertex, with edges
  between users indicating a Facebook friendship.

- **Air Travel**: A flight from Location A to Location B can be represented with
  a weighted graph, where the locations are vertices and edges indicate a valid
  flight with edge values specifying distance.

## Representations

### Adjacency List

```py
{
  "phil": ['larry', 'martin']
  "larry": ['phil']
  "martin": ['phil', 'sue']
  "sue": ['martin']
}
```

### Adjacency Matrix

```py
[
  [0, 1, 1, 0],
  [1, 0, 0, 0],
  [1, 0, 0, 1],
  [0, 0, 1, 0],
]
```

- You may need to build a graph from another structure. See
  [check_path_exists](check_path_exists.py) for a list example.

## Traversal

### Time Complexities

| Algorithm | Big-O    |
| --------- | -------- |
| DFS       | O(V + E) |
| BFS       | O(V + E) |

### Matrices

```py
def traverse_matrix_dfs(graph):
  # 1. generate row/col indices for traversal and bound checking
  # 2. instantiate set and define neighbor constant
  # 3. traverse indices and call dfs

  rows, cols = range(len(graph)), range(len(graph[0]))
  visited = set()
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  def dfs(row, col):
    # 1. check bounds and whether visited
    # 2. add to visited
    # 3. recursively call neighbors

    if (
      row not in rows
      or col not in cols
      or (row, col) in visited
    ):
      return

    visited.add((row, col))

    for x, y in neighbors:
      dfs(row + x, col + y, visited)

    for row in rows:
      for col in cols:
        if (row, col) not in visited:
          dfs(row, col)
```

```py
def traverse_matrix_bfs(graph):
  # 1. generate row/col indices for traversal and bound checking
  # 2. instantiate set and define neighbor constant
  # 3. traverse indices and call bfs

  rows, cols = range(len(graph)), range(len(graph[0]))
  visited = set()

  def bfs(row, col):
    queue = deque([(row, col)])

    while queue:
      curr_row, curr_col = queue.popleft()
      if (curr_row, curr_col) not in visited:
        visited.add((curr_row, curr_col))

        for x, y in neighbors:
          next_row, next_col = row + x, col + y

          if (next_row in rows and next_col in cols):
            queue.append((next_row, next_col))

    for row in rows:
      for col in cols:
        if (row, col) not in visited:
          bfs(row, col)
```

### Lists

```py
def traverse_list_dfs(graph):
  def dfs(vertex):
    for edge in graph[vertex]:
      dfs(edge)

    for vertex in graph:
      dfs(vertex)
```

```py
def traverse_list_bfs(graph):
  def bfs(vertex):
    queue = deque(vertex)

    while queue:
      curr = queue.popleft()

      for edge in graph[vertex]:
        bfs(edge)

    for vertex in graph:
      dfs(vertex)
```

## Considerations

- **Visited Nodes**: Keep track of visited nodes using a `set` and only visit
  each node once; it's possible to produce an infinite loop otherwise.

### Edge Cases

- Empty graph
- Graph with one or two nodes
- Disconnected graphs
- Graphs with cycles

## Exercises

### Essential

- [Number of Islands](number_of_islands.py)
- [Flood Fill](flood_fill.py)
- [01 Matrix](https://leetcode.com/problems/01-matrix/)

### Reccommended

- Rotting Oranges
- Minimum Knight Moves
- Clone Graph
- Pacific Atlantic Water Flow
- Number of Connected Components in an Undirected Graph
- Graph Valid Tree
