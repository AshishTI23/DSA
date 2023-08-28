# August-27-2023

# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

# Example:
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

from typing import List


class Solution:
    def recursive_unique_paths_with_min_sum(self, grid: List[List[int]]) -> int:
        i = len(grid)
        j = len(grid[0])

        def unique_paths(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float("inf")
            up = grid[i][j] + unique_paths(i - 1, j)
            left = grid[i][j] + unique_paths(i, j - 1)
            return min(left, up)

        return unique_paths(i - 1, j - 1)

    def memoized_unique_paths_with_min_sum(self, grid: List[List[int]]) -> int:
        i = len(grid)
        j = len(grid[0])
        dp = [[-1 for column in range(i)] for row in range(j)]

        def unique_paths(i: int, j: int) -> int:
            if dp[i][j] != -1:
                return dp[i][j]
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float("inf")

            up = grid[i][j] + unique_paths(i - 1, j)
            left = grid[i][j] + unique_paths(i, j - 1)
            dp[i][j] = min(up, left)
            return min(up, left)

        return unique_paths(i - 1, j - 1)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(Solution().memoized_unique_paths_with_min_sum(matrix))
