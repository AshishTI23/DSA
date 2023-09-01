# September-01-2023

# We are given an ‘N*M’ matrix. Every cell of the matrix has some chocolates on it,
# mat[i][j] gives us the number of chocolates. We have two friends ‘Alice’ and ‘Bob’.
# initially, Alice is standing on the cell(0,0) and Bob is standing on the cell(0, M-1).
# Both of them can move only to the cells below them in these three directions: to the bottom cell
# (↓), to the bottom-right cell(↘), or to the bottom-left cell(↙).
#
# When Alica and Bob visit a cell, they take all the chocolates from that cell with them.
# It can happen that they visit the same cell, in that case, the chocolates need to be considered only once.
#
# They cannot go out of the boundary of the given matrix, we need to return the maximum
# number of chocolates that Bob and Alice can together collect.

from typing import List


def maximum_chocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp = [[[-1 for j in range(c)] for i in range(c)] for k in range(r)]

    # write your code here
    def max_chocolates(i, j1, j2):
        if j1 < 0 or j2 < 0 or j1 >= c or j2 >= c:
            return float("-inf")
        if i == (r - 1):
            return grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        maxi = float("-inf")
        for x in range(-1, 2):
            for y in range(-1, 2):
                if j1 == j2:
                    l1 = grid[i][j1] + max_chocolates(i + 1, j1 + x, j2 + y)
                else:
                    l1 = (
                        grid[i][j1]
                        + grid[i][j2]
                        + max_chocolates(i + 1, j1 + x, j2 + y)
                    )
                maxi = max(maxi, l1)
        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]

    return max_chocolates(0, 0, c - 1)


matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
n = len(matrix)
m = len(matrix[0])
print(maximum_chocolates(n, m, matrix))
