# August-27-2023

# A thief needs to rob money in a street. The houses in the street are arranged in a circular manner.
# Therefore the first and the last house are adjacent to each other. The security system in the street
# is such that if adjacent houses are robbed, the police will get notified.
#
# Given an array of integers “Arr” which represents money at each house,
# we need to return the maximum amount of money that the thief can rob without alerting the police.
# YT: https://www.youtube.com/watch?v=3WaxQMELSkw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=7
from typing import List


class Solution:
    def __init__(self, array: List[int]):
        self.array = array

    def optimal_max_sum(self, start_index, end_index):
        prev2 = 0
        prev1 = self.array[start_index]
        for i in range(start_index + 1, end_index):
            pick = self.array[i] + prev2
            not_pick = prev1
            curr = max(pick, not_pick)
            prev2 = prev1
            prev1 = curr
        return curr


array = [18, 2, 1, 9, 9, 19]
# print(Solution(array).max_sum_memoization(len(array) - 1))
excluding_last = Solution(array).optimal_max_sum(1, len(array))
excluding_first = Solution(array).optimal_max_sum(0, len(array) - 1)
print(max(excluding_first, excluding_last))
