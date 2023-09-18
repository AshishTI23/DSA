# September-03-2023

# Partition A Set Into Two Subsets With Minimum Absolute Sum Difference
#
# We are given an array ‘ARR’ with N positive integers. We need to partition the array
# into two subsets such that the absolute difference of the sum of elements of the subsets is minimum.
#
# We need to return only the minimum absolute difference of the sum of elements of the two partitions.
from typing import List


class Solution:
    def __init__(self, array: List[List[int]]):
        self.array = array
        self.n: int = len(array)
        self.total: int = sum(array)

    def recursive(self):
        def min_diff(n: int, total_s1: int) -> int:
            if n == 0:
                return abs(2 * total_s1 - self.total)
            take = min_diff(n - 1, total_s1 + self.array[n])
            not_take = min_diff(n - 1, total_s1)
            return min(take, not_take)

        return min_diff(self.n - 1, 0)


print(Solution([1, 2, 6]).recursive())
