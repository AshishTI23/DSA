# August-19-2023

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
#
# Input: s = "()[]{}"
# Output: true
from typing import List, Dict

class Solution:
    def __init__(self, string: str):
        self.string = string

    def brute_force(self) -> bool:
        stack: List[str] = list()
        brackets_map: Dict[str, str] = {")": "(", "}": "{", "]": "["}
        opening_bracket: Dict[str, str] = {"(": ")","{": "}","[": "]"}
        if len(self.string) == 1:
            return False
        for item in self.string:
            if item in opening_bracket:
                stack.append(item)
            else:
                try:
                    last_element = stack.pop()
                    if last_element == brackets_map[item]:
                        pass
                    else:
                        return False
                except IndexError:
                    return False
        if stack:
            return False
        return True

#YouTube: https://www.youtube.com/watch?v=wkDfsKijrZ8&t=282s&pp=ygURdmFsaWQgcGFyYW50aGVzaXM%3D