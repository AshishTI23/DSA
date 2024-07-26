# From a given array find max sum with subarray length is k
# Ex -> input_array = [-1, 2, 3, 3, 4, 5, -1], k=4
# Output -> 15

class Solution:
    def __init__(self, array) -> None:
        self.array = array

    def get_prefix_sum_array(self):
        prev_sum = 0
        for i in range(len(self.array)):
            self.array[i] = prev_sum + self.array[i]
            prev_sum = self.array[i]
        print(self.array)
        return self.array

    def optimized_time(self, k: int):
        self.get_prefix_sum_array()
        max_sum = 0
        left = 0
        for right in range(k, len(self.array)):
            if left == 0:
                max_sum = self.array[k]
            max_sum = max(max_sum, self.array[right] - self.array[left])
            left += 1
        return max_sum


s = Solution([-1, 2, 3, 3, 4, 5, -1])
print(s.optimized_time(4))