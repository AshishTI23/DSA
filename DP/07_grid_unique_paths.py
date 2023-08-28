# August-28-2023

# Given two values M and N, which represent a matrix[M][N]. We need to find the total unique paths
# from the top-left cell (matrix[0][0]) to the rightmost cell (matrix[M-1][N-1]).
#
# At any cell we are allowed to move in only two directions:- bottom and right.
from typing import List


class Solution:
    def recursive_unique_paths(self, i: int, j: int) -> int:
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        up = self.recursive_unique_paths(i - 1, j)
        left = self.recursive_unique_paths(i, j - 1)
        return left + up

    def memoized_unique_paths(self, i: int, j: int, dp: List[List[int]]) -> int:
        if dp[i][j] != -1:
            return dp[i][j]
        if i == 0 and j == 0:
            dp[i][j] = 1
            return dp[i][j]
        if i < 0 or j < 0:
            return 0
        up = self.memoized_unique_paths(i - 1, j, dp)
        left = self.memoized_unique_paths(i, j - 1, dp)
        dp[i][j] = left + up
        return dp[i][j]

    def tabular_unique_paths(self, i, j) -> int:
        prev_row = [0 for column in range(i + 1)]
        prev_row[0] = 1
        for row in range(i + 1):
            prev = 1
            for column in range(1, j + 1):
                prev_row[column] = prev_row[column] + prev
                prev = prev_row[column]
        return prev


m = 3
n = 3
grid = [[-1 for column in range(n)] for row in range(m)]
print(Solution().tabular_unique_paths(m - 1, n - 1))
