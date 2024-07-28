# From given string find the maximum length of substring with k distinct chars
# Ex: s = "aaabbccd", K = 2
# Output = 5
# Explaination -> aaabb is substr with max length of K distinct chars

class Solution:
    def __init__(self, string: str) -> None:
        self.string = string

    def optimal(self, k: int) -> int:
        max_len = left = 0
        hash = {}
        for right in range(len(self.string)):
            # Always store the first index of any char
            if hash.get(self.string[right], None) == None:
                hash[self.string[right]] = 1
            else:
                hash[self.string[right]] += 1
            # Loop until hash has K items and increase left
            while len(hash) > k:
                hash[self.string[right]] -= 1
                left += 1
                # Remove the item from hash as soon as count of item becomes zero
                if hash[self.string[right]] == 0:
                    hash.pop(self.string[right])
            max_len = max(max_len, right - left + 1)
        return max_len
    
s = Solution("aaabbccd")
print(s.optimal(3))

