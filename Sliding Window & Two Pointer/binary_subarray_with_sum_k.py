# Given a binary array nums and an integer goal, return the number of 
# non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.
# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4

# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

from typing import List

class Solution:
    def __init__(self, array: List[int], goal: int) -> None:
        self.array = array
        self.goal = goal

    def brute_force(self) -> int:
        count = 0
        for left in range(len(self.array)):
            sum = 0
            for right in range(left, len(self.array)):
                sum += self.array[right]
                if sum == self.goal:
                    count += 1
        return count
    
    def optimal(self) -> int:
        def helper(array: List[int], goal: int) -> int:
            if goal < 0:
                return 0
            sum = count = left = 0
            for right in range(len(array)):
                sum += array[right]
                while sum > goal:
                    sum -= array[left]
                    left += 1
                count += (right - left + 1)
            return count
        return helper(self.array, self.goal) - helper(self.array, self.goal - 1)
    
    # Change all odd numbers in array to 1 and even to 0
    def convert_to_nice_array(self):
        for index in range(len(self.array)):
            if self.array[index] % 2 == 0:
                self.array[index] = 0
            else:
                self.array[index] = 1
    

array = [1,0,0,1,1,0]
goal = 2
sol = Solution(array, goal)
print(sol.optimal())
# https://www.youtube.com/watch?v=j4JDr4-jvo4