# August-20-2023

# Given an array of integers nums which is sorted in ascending order, and an integer target ,
# write a function to search target in nums . If target exists,thenreturnitsindex.Otherwise,return -1 .
# You must write an algorithm with 0(log n) runtime complexity.
from typing import List


class Solution:
    def __init__(self, array: List[int], target: int):
        self.array = array
        self.target = target

    def recursive_binary_search(self, low, high) -> int:
        if low >= high:
            return -1
        mid = (low + high) // 2
        if self.array[mid] == self.target:
            return mid
        elif self.array[mid] < self.target:
            return self.recursive_binary_search(mid, high)
        else:
            return self.recursive_binary_search(low, mid)

    def iterative_binary_search(self) -> int:
        low: int = 0
        high: int = len(self.array) - 1
        while low < high:
            mid = (low + high) // 2
            if self.array[mid] == self.target:
                return mid
            elif self.array[mid] < self.target:
                low = mid + 1
            else:
                high = mid - 1

        return high if low == high and self.array[low] == self.target else -1
