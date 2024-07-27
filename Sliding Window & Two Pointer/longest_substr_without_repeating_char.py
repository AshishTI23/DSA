#  Longest Substring Without Repeating Characters
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def __init__(self, string: str) -> None:
        self.string = string

    def brute_force(self) -> int:
        max_length = 0
        for i in range(len(self.string)):
            hash = {}
            for j in range(i, len(self.string)):
                if self.string[j] in hash:
                    max_length = max(max_length, j-i)
                    break
                hash[self.string[j]] = 1
        return max_length
    
    def optimal(self) -> int:
        left = max_len = 0
        hash = {}
        for right in range(len(self.string)):
            if self.string[right] in hash and hash[self.string[right]] >= left:
                left = hash[self.string[right]] + 1
            hash[self.string[right]] = right
            max_len = max(max_len, right-left + 1)
        return max_len
        
string = " "
string = "takeuforward"
string = "abcabcbb"
# string = "aab"
sol = Solution(string)
print(sol.optimal())

        