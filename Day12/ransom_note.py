# August-24-2023

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
from typing import Dict


class Solution:
    def __init__(self, ransom_note: str, magazine: str):
        self._ransom_note = ransom_note
        self.magazine = magazine

    def ransom_note(self) -> bool:
        hash_map: Dict[str, int] = {}
        for item in self._ransom_note:
            if item in hash_map:
                hash_map[item] += 1
            else:
                hash_map[item] = 1
        for item in self.magazine:
            if item in hash_map:
                hash_map[item] -= 1
                if hash_map[item] < 0:
                    return False
            else:
                return False
        return True
