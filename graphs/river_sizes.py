# Given a two dimensional array of 0 and 1s, return an array of the sizes of all
# rivers contained within the input matrix.

# A river consists of any number of 1s either horizontally or vertically adjacent.
# The number of adjacent 1s forming a river determine its size.


def river_sizes(matrix):
    rows, cols = range(len(matrix)), range(len(matrix[0]))
    sizes = []
    visited = set()

    def dfs(row, col):
        if (
            row not in rows
            or col not in cols
            or (row, col) in visited
            or matrix[row][col] != 1
        ):
            return 0

        visited.add((row, col))
        size = 0

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for x, y in neighbors:
            size += dfs(row + x, col + y)

        return size + 1

    for row in rows:
        for col in cols:
            if (row, col) not in visited and matrix[row][col] == 1:
                size = dfs(row, col)
                sizes.append(size)

    return sizes
