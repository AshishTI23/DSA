# September-02-2023

# We are given an array ‘ARR’ with N positive integers. We need to find if we
# can partition the array into two subsets such that the sum of elements of each
# subset is equal to the other.
#
# If we can partition, return true else return false
from typing import List


class Solution:
    def __init__(self, array: List[List[int]]):
        self.array = array
        self.total = sum(array)

    def check_two_sunsets_with_equal_sum(self):
        if self.total % 2 != 0:
            return False
        target = self.total // 2
        length = len(self.array)
        dp: List[List[int]] = [[-1 for j in range(target + 1)] for i in range(length)]

        def find_subset(n, target):
            if target == 0:
                return True
            if n == 0:
                return (target - self.array[0]) == 0
            if dp[n][target] != -1:
                return dp[n][target]
            take = find_subset(n - 1, target - self.array[n])
            not_take = find_subset(n - 1, target)
            dp[n][target] = take or not_take
            return dp[n][target]

        return find_subset(length - 1, target)


arr = [1, 2, 3, 4]

print(Solution(arr).check_two_sunsets_with_equal_sum())
