def number_of_islands(grid):
    rows, cols = range(len(grid)), range(len(grid[0]))

    def dfs(row, col, visited):
        if (
            row not in rows
            or col not in cols
            or (row, col) in visited
            or grid[row][col] != "1"
        ):
            return 0

        visited.add((row, col))

        neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for x, y in neighbors:
            dfs(row + x, col + y, visited)

        return 1

    visited = set()

    total = 0

    for row in rows:
        for col in cols:
            total += dfs(row, col, visited)

    return total
