# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.


def flood_fill(image, sr, sc, color):
    starting_pixel = image[sr][sc]
    visited = set()

    def dfs(row, col, visited, image):
        if (
            row not in range(len(image))
            or col not in range(len(image[0]))
            or (row, col) in visited
        ):
            return

        visited.add((row, col))

        pixel = image[row][col]
        if pixel != starting_pixel:
            return

        image[row][col] = color

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for x, y in neighbors:
            dfs(row + x, col + y, visited, image)

    dfs(sr, sc, visited, image)

    return image
