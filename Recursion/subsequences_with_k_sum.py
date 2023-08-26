# August-26-2023

# Print All Subsequnces whose sum is K
from typing import List, Any


class Solution:
    def __init__(self, sequence: List[int], target: int):
        self.sequence = sequence
        self.target = target

    def find_subsequnces_with_target_sum(
        self, index: int = 0, subsequence_array: List[int] = [], sum_: int = 0
    ) -> Any:
        if index >= len(self.sequence):
            if sum_ == self.target:
                print(subsequence_array)
            return
        subsequence_array.append(self.sequence[index])
        sum_ += self.sequence[index]
        self.find_subsequnces_with_target_sum(index + 1, subsequence_array, sum_)
        poped = subsequence_array.pop()
        sum_ -= poped
        self.find_subsequnces_with_target_sum(index + 1, subsequence_array, sum_)

    def find_one_subsequnce_with_target_sum(
        self, index: int = 0, subsequence_array: List[int] = [], sum_: int = 0
    ) -> Any:
        if index >= len(self.sequence):
            if sum_ == self.target:
                print(subsequence_array)
                return True
            return False
        subsequence_array.append(self.sequence[index])
        sum_ += self.sequence[index]
        if self.find_one_subsequnce_with_target_sum(index + 1, subsequence_array, sum_):
            return True
        poped = subsequence_array.pop()
        sum_ -= poped
        if self.find_one_subsequnce_with_target_sum(index + 1, subsequence_array, sum_):
            return True
        return False

    def count_of_subsequnce_with_target_sum(
        self, index: int = 0, subsequence_array: List[int] = [], sum_: int = 0
    ) -> int:
        if index >= len(self.sequence):
            if sum_ == self.target:
                return 1
            return 0
        subsequence_array.append(self.sequence[index])
        sum_ += self.sequence[index]
        left = self.count_of_subsequnce_with_target_sum(
            index + 1, subsequence_array, sum_
        )
        poped = subsequence_array.pop()
        sum_ -= poped
        right = self.count_of_subsequnce_with_target_sum(
            index + 1, subsequence_array, sum_
        )
        return left + right


print(Solution([1, 2, 1], 2).count_of_subsequnce_with_target_sum())
# https://www.youtube.com/watch?v=eQCS_v3bw0Q
