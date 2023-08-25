# August-25-2023

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution:
    def climb_stairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def recursive_call(n: int):
            if n <= 1:
                return 1
            if dp[n] == -1:
                dp[n] = recursive_call(n - 1) + recursive_call(n - 2)
            return dp[n]

        return recursive_call(n)

    def optimal_climb_stairs(self, n: int) -> int:
        prev1, prev2 = 0, 1
        for i in range(1, n + 1):
            prev1, prev2 = prev2, prev2 + prev1
        return prev2


# print(Solution().climb_stairs(0))
# print(Solution().optimal_climb_stairs(0))
