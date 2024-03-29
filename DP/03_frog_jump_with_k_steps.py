# August-26-2023

# Frog Jump with k Distances
# This is a follow-up question to “Geek Jump”. In the previous
# question, the frog was allowed to jump either one or two steps at a time. In this question, the frog
# is allowed to jump up to ‘K’ steps at a time. If K=4, the frog can jump 1,2,3, or 4 steps at every index.
from typing import List


class Solution:
    def __init__(self, heights: List[int], n: int, k: int):
        self.heights = heights
        self.n = n
        self.k = k
        self.dp: List[int] = [-1] * (n + 1)

    def energy_spent(self, n):
        if n == 0:
            return 0
        if self.dp[n] != -1:
            return self.dp[n]
        min_step = float("inf")
        for j in range(1, self.k + 1):
            if n - j >= 0:
                jump = self.energy_spent(n - j) + abs(
                    self.heights[n] - self.heights[n - j]
                )
                min_step = min(jump, min_step)
        self.dp[n] = min_step
        return self.dp[n]

    def optimal_energy_spent(self):
        self.dp[0] = 0
        for i in range(1, self.n):
            min_step = float("inf")
            for j in range(1, self.k + 1):
                if i - j >= 0:
                    jump = self.dp[i - j] + abs(self.heights[i] - self.heights[i - j])
                    min_step = min(jump, min_step)
            self.dp[i] = min_step
        print(self.dp)
        return self.dp[self.n - 1]


# heights: List[int] = [30, 10, 60, 10, 60, 50]

# print(Solution(heights, len(heights), 2).energy_spent(len(heights) - 1))
# print(Solution(heights, len(heights), 4).optimal_energy_spent())
