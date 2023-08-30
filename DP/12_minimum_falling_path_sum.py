# August-30-2023
import copy

# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element in the next row that
# is either directly below or diagonally left/right. Specifically, the next element
# from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
from typing import List


class Solution:
    def __init__(self, input_matrix: List[List[int]]):
        self.input_matrix = input_matrix

    def recursive(self):
        row = len(self.input_matrix) - 1
        column = len(self.input_matrix[0]) - 1

        def min_path_sum(i, j) -> int:
            if j < 0 or j > column:
                return float("inf")
            if i == 0:
                return self.input_matrix[i][j]

            left = self.input_matrix[i][j] + min_path_sum(i - 1, j - 1)
            right = self.input_matrix[i][j] + min_path_sum(i - 1, j + 1)
            up = self.input_matrix[i][j] + min_path_sum(i - 1, j)

            return min(up, min(right, left))

        mini = float("inf")
        for j in range(column + 1):
            mini = min(mini, min_path_sum(row, j))
        return mini

    def memozation(self):
        row = len(self.input_matrix) - 1
        column = len(self.input_matrix[0]) - 1
        dp = [[-1 for j in range(row + 1)] for i in range(column + 1)]

        def min_path_sum(i, j, dp):
            if j < 0 or j > column:
                return float("inf")
            if i == 0:
                return matrix[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            left = self.input_matrix[i][j] + min_path_sum(i - 1, j - 1, dp)
            right = self.input_matrix[i][j] + min_path_sum(i - 1, j + 1, dp)
            up = self.input_matrix[i][j] + min_path_sum(i - 1, j, dp)
            dp[i][j] = min(up, min(right, left))
            return dp[i][j]

        mini = float("inf")
        for j in range(column + 1):
            mini = min(mini, min_path_sum(row, j, dp))
        return mini

    def tabular(self):
        row = len(self.input_matrix)
        column = len(self.input_matrix[0])
        prev = self.input_matrix[0]
        curr = [0] * (column)
        for i in range(1, row):
            up = right = left = float("inf")
            for col in range(column):
                up = self.input_matrix[i][col] + prev[col]
                if (col - 1) >= 0:
                    left = self.input_matrix[i][col] + prev[col - 1]
                if (col + 1) < column:
                    right = self.input_matrix[i][col] + prev[col + 1]
                curr[col] = min(up, min(left, right))
            prev = curr[:]
        mini = float("inf")
        for item in prev:
            mini = min(mini, item)
        return mini


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
# matrix = [[-19,57],[-40,-5]]
print(Solution(matrix).tabular())
