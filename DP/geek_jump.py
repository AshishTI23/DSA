# August-25-2023

# Geek wants to climb from the 0th stair to the(n - 1)th stair. At a time the Geek can climb
# either one or two steps.A height[N] array is also given.Whenever the geek jumps from stair
# i to stair j,the energy consumed in the jump is abs(height[i] - height[j]), where abs() means the
# absolute adifference. return the minimum energy that can be used by the Geek to jump from stair 0 to stair N-1

# Example:
# Input:
# n = 4
# height = {10 20 30 10}
# Output:
# 20
# Explanation:
# Geek jump from 1st to 2nd stair(|20-10| = 10 energy lost).
# Then a jump from the 2nd to the last stair(|10-20| = 10 energy lost).
# so, total energy lost is 20 which is the minimum.

# August-24-2023

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
from typing import List


class Solution:
    def min_energy_spent(self, n: int, heights: List[int]) -> int:
        dp = [-1] * (n)
        n = n - 1

        def geek_jump(n):
            if n <= 0:
                return 0
            if dp[n] == -1:
                left = geek_jump(n - 1) + abs(heights[n] - heights[n - 1])
                if n >= 2:
                    right = geek_jump(n - 2) + abs(heights[n] - heights[n - 2])
                else:
                    right = float("inf")
                dp[n] = min(left, right)
            return dp[n]

        return geek_jump(n)

    def optimal_min_energy_spent(self, n: int, heights: List[int]) -> int:
        prev = 0
        prev2 = 0

        for i in range(1, n):
            diff1 = prev + abs(heights[i] - heights[i - 1])
            if i >= 2:
                diff2 = prev2 + abs(heights[i] - heights[i - 2])
            else:
                diff2 = float("inf")
            curr = min(diff1, diff2)
            prev2 = prev
            prev = curr
        return prev


print(Solution().min_energy_spent(6, [30, 10, 60, 10, 60, 50]))
