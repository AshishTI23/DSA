# September-15-2023

# A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items.
# Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can either include
# an item in its knapsack or exclude it but can’t partially have it as a fraction. We need to
# find the maximum value of items that the thief can steal.

from typing import List


class Solution:
    def __init__(self, wt: List[int], val: List[int], target_wt: int):
        self.wt = wt
        self.val = val
        self.target_wt = target_wt

    def recursive(self):
        target_wt = self.target_wt
        index = len(self.wt)

        def knapsack(index, target_wt):
            if index == 0:
                if target_wt >= self.wt[index]:
                    return self.val[index]
                else:
                    return 0
            not_take = knapsack(index - 1, target_wt)
            take = float("-inf")
            if target_wt >= self.wt[index]:
                take = val[index] + knapsack(index - 1, target_wt - self.wt[index])
            return max(take, not_take)

        return knapsack(index - 1, target_wt)

    def memoization(self):
        target_wt = self.target_wt
        index = len(self.wt)
        dp = [[-1 for col in range(target_wt + 1)] for row in range(index)]

        def knapsack(index, target_wt, dp):
            if dp[index][target_wt] != -1:
                return dp[index][target_wt]
            if index == 0:
                if target_wt >= self.wt[index]:
                    return self.val[index]
                else:
                    return 0
            not_take = knapsack(index - 1, target_wt, dp)
            take = float("-inf")
            if target_wt >= self.wt[index]:
                take = val[index] + knapsack(index - 1, target_wt - self.wt[index], dp)
            dp[index][target_wt] = max(take, not_take)
            return dp[index][target_wt]

        return knapsack(index - 1, target_wt, dp)


wt = [3, 4, 5]
val = [30, 50, 60]
target_wt = 8
print(Solution(wt, val, target_wt).memoization())
