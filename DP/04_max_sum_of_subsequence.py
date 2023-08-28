# August-27-2023

# https://takeuforward.org/data-structure/maximum-sum-of-non-adjacent-elements-dp-5/
# Maximum sum of non-adjacent elements (DP 5)
# In this article we will solve the problem: Maximum sum of non-adjacent elements (DP 5)
#
# Problem Statement:
#
# Given an array of ‘N’  positive integers, we need to return the maximum sum of the subsequence such that
# no two elements of the subsequence are adjacent elements in the array.
#
# Note: A subsequence of an array is a list with elements of the array where some elements are deleted
# ( or not deleted at all) and the elements should be in the same order in the subsequence as in the array.
# YT: https://www.youtube.com/watch?v=GrMBfJNk_NY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=6
from typing import List


class Solution:
    def __init__(self, array: List[int]):
        self.array = array
        self.dp: List[int] = [-1] * len(array)

    def recursive_max_sum(self, index) -> int:
        if index == 0:
            return self.array[index]
        if index < 0:
            return 0
        pick = self.array[index] + self.recursive_max_sum(index - 2)
        not_pick = self.recursive_max_sum(index - 1)
        return max(pick, not_pick)

    def max_sum_memoization(self, index) -> int:
        if self.dp[index] != -1:
            return self.dp[index]
        if index == 0:
            return self.dp[0]
        if index < 0:
            return 0
        pick = self.array[index] + self.max_sum_memoization(index - 2)
        not_pick = self.max_sum_memoization(index - 1)
        self.dp[index] = max(pick, not_pick)
        return self.dp[index]

    def optimal_max_sum(self):
        prev2 = 0
        prev1 = self.array[0]
        for i in range(1, len(self.array)):
            pick = self.array[i] + prev2
            not_pick = prev1
            curr = max(pick, not_pick)
            prev2 = prev1
            prev1 = curr
        return curr


array = [1, 2, 1, 9, 19, 9]
# print(Solution(array).max_sum_memoization(len(array) - 1))
print(Solution(array).optimal_max_sum())
