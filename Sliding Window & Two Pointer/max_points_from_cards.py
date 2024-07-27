# Maximum Points You Can Obtain from Cards

# There are several cards arranged in a row, and each card has an associated 
# number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of 
# the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

# Example 1:

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. 
# However, choosing the rightmost card first will maximize your total score. 
# The optimal strategy is to take the three cards on the right, giving a 
# final score of 1 + 6 + 5 = 12.
from typing import List

class Solution:
    def __init__(self, array: List[int]) -> None:
        self.array = array

    def optimal(self, k: int) -> int:
        if k == len(self.array):
            return sum(self.array)
        left_sum = right_sum = max_sum = 0
        for i in range(k):
            left_sum += self.array[i]
        max_sum = left_sum
        right = len(self.array) - 1
        for j in range(k):
            right_sum += self.array[right]
            left_sum -= self.array[k-j-1]
            max_sum = max(max_sum, right_sum + left_sum)
            right -= 1
        return max_sum

s = Solution([1,2,3,4,5,6,9])
print(s.optimal(5))