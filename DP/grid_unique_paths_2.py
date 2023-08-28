# August-28-2023

# We are given an “N*M” Maze. The maze contains some obstacles. A cell
# is ‘blockage’ in the maze if its value is -1. 0 represents non-blockage.
# There is no path possible through a blocked cell.
#
# We need to count the total number of unique paths from the top-left corner of
# the maze to the bottom-right corner. At every cell, we can move either down or towards the right.

from typing import List


class Solution:
    def recursive_unique_paths(self, grid: List[List[int]]) -> int:
        i = len(grid)
        j = len(grid[0])

        def unique_paths(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if grid[i][j] == 1:
                return 0
            up = unique_paths(i - 1, j)
            left = unique_paths(i, j - 1)
            return left + up

        return unique_paths(i - 1, j - 1)

    def memoized_unique_paths(self, grid: List[List[int]]) -> int:
        i = len(grid)
        j = len(grid[0])
        dp = [[-1 for column in range(i)] for row in range(j)]

        def unique_paths(i: int, j: int) -> int:
            if i > 0 and j > 0 and grid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            up = unique_paths(i - 1, j)
            left = unique_paths(i, j - 1)
            dp[i][j] = left + up
            return dp[i][j]

        return unique_paths(i - 1, j - 1)


matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

print(Solution().memoized_unique_paths(matrix))
