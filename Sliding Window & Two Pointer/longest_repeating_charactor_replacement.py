# You are given a string s and an integer k. You can choose any character of 
# the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you 
# can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

class Solution:
    def __init__(self, string: str) -> None:
        self.string = string

    def brute_force(self, k: int) -> int:
        max_len = 0
        for i in range(len(self.string)):
            hash = {}
            max_frequency = 0
            for j in range(i, len(self.string)):
                if hash.get(self.string[j], None) is None:
                    hash[self.string[j]] = 1
                else:
                    hash[self.string[j]] += 1
                max_frequency = max(max_frequency, hash[self.string[j]])
                max_len = max(max_len, max_frequency + k)
                if max_len >= len(self.string):
                    return len(self.string)
                if (j - i) == (max_frequency + k):
                    break
        return max_len
    
    def optimal(self, k: int) -> int:
        max_len = max_frequency = left = 0
        hash = {}
        for right in range(len(self.string)):
            if hash.get(self.string[right], None) is None:
                    hash[self.string[right]] = 1
            else:
                hash[self.string[right]] += 1
            max_frequency = max(max_frequency, hash[self.string[right]])
            if (right - left + 1) - max_frequency <= k:
                max_len = max(max_len, (right - left + 1))
            if (right - left + 1) - max_frequency > k:
                hash[self.string[left]] -= 1
                left += 1
        return max_len
    
# string = "ABAB"
# k = 2

string = "AABAABBA"
k = 1

s = Solution(string)
print(s.optimal(k))