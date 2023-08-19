# August-19-2023

# You are given an array prices where prices[i] is the price of a given
# stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one
# stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0

# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List
class Solution:

    def __int__(self, prices: List[int]):
        self.prices = prices

    def brute_force(self) -> int:
        max_profit: int = 0
        for i in range(len(self.prices)):
            for j in range(i+1, len(self.prices)):
                if self.prices[i] > self.prices[j]:
                    pass
                else:
                    max_profit = max(max_profit, self.prices[j] - self.prices[i])
        return max_profit

    def optimal(self) -> int:
        max_profit: int = 0
        min_buying: int = self.prices[0]
        for i in range(1, len(self.prices)):
            max_profit = max(max_profit, self.prices[i] - min_buying)
            min_buying = min(self.prices[i],min_buying)
        return max_profit