# Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of 
# consecutive 1's in the array if you can flip at most k 0's.

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Approach - Max consecutive subarray with k 0s

class Solution:
    def __init__(self, array) -> None:
        self.array = array
    
    def optimal(self, k: int) -> int:
        max_len = zeros = left = right = 0
        for right in range(len(self.array)):
            print(left, right, self.array[right], self.array[left], zeros)
            if self.array[right] == 0:
                zeros += 1
            if zeros > k and self.array[right] == 0:
                if self.array[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                max_len = max(max_len, right - left + 1)
        return max_len
    
s = Solution([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1])
print(s.optimal(3))