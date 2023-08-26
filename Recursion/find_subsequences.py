# August-26-2023

# Print All Subsequnces
from typing import List


class Solution:
    def __init__(self, sequence: List[int]):
        self.sequence = sequence

    def print_subsequnces(self, index: int = 0, subsequence_array: List[int] = []):
        if index >= len(self.sequence):
            print(subsequence_array)
            return
        subsequence_array.append(self.sequence[index])
        self.print_subsequnces(index + 1, subsequence_array)
        subsequence_array.pop()
        self.print_subsequnces(index + 1, subsequence_array)


Solution([3, 1, 2]).print_subsequnces()
# https://www.youtube.com/watch?v=AxNNVECce8c&t=1255s
