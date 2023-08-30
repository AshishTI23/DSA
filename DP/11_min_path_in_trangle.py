# August-30-2023

# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.

# Example 1:
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
from typing import List


class Solution:
    def minimum_path_sum(self, triangle: List[List[int]]) -> int:
        n = len(triangle) - 1
        # def recursive_min_sum(i, j):
        #     if i == n:
        #         return triangle[i][j]
        #     d = triangle[i][j] + recursive_min_sum(i + 1, j)
        #     dr = triangle[i][j] + recursive_min_sum(i + 1, j + 1)
        #     return min(d, dr)
        #
        # return recursive_min_sum(0, 0)

        def memoization_min_sum(n):
            for i in range(n - 1, -1, -1):
                for j in range(i + 1):
                    triangle[i][j] = min(
                        triangle[i][j] + triangle[i + 1][j],
                        triangle[i][j] + triangle[i + 1][j + 1],
                    )
            return triangle[0][0]

        return memoization_min_sum(n)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimum_path_sum(triangle))
