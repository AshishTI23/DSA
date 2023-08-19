# August-19-2023

# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element
# twice.

# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
from typing import List, Dict

class Solution:
    def __init__(self, nums: List[int], target: int):
        self.array = nums
        self.target = target

    def brute_force(self) -> List[int]:
        for i in range(len(self.array)):
            for j in range(i+1, len(self.array)):
                if self.array[i] + self.array[j] == self.target:
                    return [i, j]
        return []

    def with_hash(self) -> List[int]:
        hash_map: Dict[int, int] = hash()
        for index in range(len(self.array)):
            pair_item: int = self.target - self.array[index]
            if pair_item in hash_map:
                return [hash_map[pair_item], index]
            else:
                hash_map[self.array[index]] = index
