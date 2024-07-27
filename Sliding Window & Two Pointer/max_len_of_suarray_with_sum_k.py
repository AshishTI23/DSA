# From a given array find max length of subarray with sum k
# Ex -> input_array = [-1, 2, 3, 3, 4, 5, -1], k=15
# Output -> 4

class Solution:
    def __init__(self, array) -> None:
        self.array = array

    def brute_force(self, k: int) -> int:
        max_len = 0
        for left in range(len(self.array)):
            sum = 0
            for right in range(left, len(self.array)):
                sum += self.array[right]
                if sum == k:
                    max_len = max(max_len, right - left + 1)
        return max_len
    
    def optimal(self, k: int) -> int:
        prefix_sum_hash = {0: -1}
        # prefix_sum_hash = {prefix_sum: index}
        max_len = current_sum = 0
        for i in range(len(self.array)):
            current_sum += self.array[i]
            if (current_sum - k) in prefix_sum_hash:
                max_len = max(max_len, i - prefix_sum_hash[current_sum - k])
            else:
                prefix_sum_hash[current_sum] = i
        return max_len
    
arr = [-1, 2, 3, 3, 4, 5, -1]
s = Solution(arr)
print(s.optimal(-1))