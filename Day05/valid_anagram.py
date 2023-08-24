# August-20-2023

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once.

# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
from typing import Dict


class Solution:
    def __init__(self, first_string: str, second_string: str):
        self.first_string = first_string
        self.second_string = second_string

    def with_sorting(self) -> bool:
        return sorted(self.first_string) == sorted(self.second_string)

    def with_hash(self) -> bool:
        hash_map: Dict[str, int] = {}
        for item in self.first_string:
            if item not in hash_map:
                hash_map[item] = 1
            else:
                hash_map[item] += 1
        for item in self.second_string:
            if item not in hash_map:
                return False
            else:
                hash_map[item] -= 1
        for _, value in hash_map.items():
            if value > 0 or value < 0:
                return False
        return True
