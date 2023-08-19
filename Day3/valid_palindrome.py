# August-20-2023

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
# characters include letters and numbers.
# Given a string s return true if it is a palindrome, or false otherwise.

# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    def __init__(self, string: str) -> bool:
        self.string = string

    def optimal(self):
        start: int = 0
        end: int = len(self.string) - 1
        while start < end:
            if self.string[start].isalnum() and self.string[end].isalnum():
                if self.string[start].lower() != self.string[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
            elif not self.string[start].isalnum():
                start += 1
            elif not self.string[end].isalnum():
                end -= 1
        return True

#YouTube: https://www.youtube.com/watch?v=028pTf2kBFI&t=231s