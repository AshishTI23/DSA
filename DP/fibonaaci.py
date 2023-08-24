# August-24-2023

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
from typing import List


class Solution:
    def fibonaaci(self, n: int) -> int:
        dp_array: List[int] = [0] * (n + 1)

        def fib(n, dp_array):
            if n <= 1:
                return n
            if dp_array[n] != 0:
                return dp_array[n]
            dp_array[n] = fib(n - 1, dp_array) + fib(n - 2, dp_array)
            return dp_array[n]

        return fib(n, dp_array)

    def optimal_fibonaaci(self, n: int) -> int:
        dp_array: List[int] = [0] * (n + 1)
        # Base Case fib(0) is 0 and fib(1) is one
        dp_array[1] = 1
        for index in range(2, n + 1):
            dp_array[index] = dp_array[index - 1] + dp_array[index - 2]
        return dp_array[n]


print(Solution().optimal_fibonaaci(9))