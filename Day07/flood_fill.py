# August-22-2023

# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
# You are also given three integers sr , sc and color . You should perform a
# flood fill on the image starting from the pixel image[sr][sc] .
# Return the modified image after performing the flood fill.

# Input: image = {{1,1,1},{1,1,0},{1,0,1}},
# sr = 1, sc = 1, newColor = 2.
# Output: {{2,2,2},{2,2,0},{2,0,1}}
# Explanation: From the center of the image
# (with position (sr, sc) = (1, 1)), all
# pixels connected by a path of the same color
# as the starting pixel are colored with the new
# color.Note the bottom corner is not colored 2,
# because it is not 4-directionally connected to
# the starting pixel.
from typing import List


class Solution:
    def __init__(self, image: List[List[int]], new_color: int, sr: int, sc: int):
        self.image = image
        self.new_color = new_color
        self.prev_color = self.image[sr][sc]
        self.slide_row: List[int] = [0, -1, 0, 1]
        self.slide_column: List[int] = [-1, 0, 1, 0]
        self.max_row: int = len(self.image)
        self.max_column: int = len(self.image[0])

    def flood_fill_with_dfs(self, sr: int, sc: int) -> List[List[int]]:
        self.image[sr][sc] = self.new_color
        for index in range(4):
            nr = sr + self.slide_row[index]
            nc = sc + self.slide_column[index]
            if nr >= 0 and nr < self.max_row and nc >= 0 and nc < self.max_column:
                if (
                    self.image[nr][nc] == self.prev_color
                    and self.image[nr][nc] != self.new_color
                ):
                    self.flood_fill_with_dfs(nr, nc)
        return self.image


# Example to call the flood fill function
# image = [[1,1,1], [1,1,0], [1,0,1]]
# new_color = 2
# starting_row, starting_column = 1, 1
# s = Solution(image, new_color, starting_row, starting_column)
# print(s.flood_fill_with_dfs(starting_row, starting_column))
