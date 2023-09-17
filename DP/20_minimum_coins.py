# September-17-2023

# We are given a target sum of ‘X’ and ‘N’ distinct numbers denoting the coin denominations.
# We need to tell the minimum number of coins required to reach the target sum. We can pick a
# coin denomination for any number of times we want.

from typing import List, Any


class Solution:
    def __init__(self, array: List[int], target: int):
        self.array = array
        self.target = target

    def recursive(self) -> Any:
        target = self.target
        index = len(self.array)

        def min_coins(index: int, target: int) -> Any:
            if index == 0:
                if target % self.array[index] == 0:
                    return target // self.array[index]
                return float("inf")
            not_take = 0 + min_coins(index - 1, target)
            take = float("inf")
            if target >= self.array[index]:
                take = 1 + min_coins(index, target - self.array[index])
            return min(take, not_take)

        return min_coins(index - 1, target)

    def memoization(self) -> Any:
        target = self.target
        index = len(self.array)
        dp = [[-1 for col in range(target+1)] for row in range(index)]

        def min_coins(index: int, target: int, dp: List[int]) -> Any:
            if index == 0:
                if target % self.array[index] == 0:
                    dp[index][target] = target // self.array[index]
                    return dp[index][target]
                return float("inf")
            if dp[index][target] != -1:
                return dp[index][target]
            not_take = 0 + min_coins(index - 1, target, dp)
            take = float("inf")
            if target >= self.array[index]:
                take = 1 + min_coins(index, target - self.array[index], dp)
            dp[index][target] = min(take, not_take)
            return dp[index][target]

        return min_coins(index - 1, target, dp)


array = [1, 2, 3]
target = 6
print(Solution(array, target).memoization())
