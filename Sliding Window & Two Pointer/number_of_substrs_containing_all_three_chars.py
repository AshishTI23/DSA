#  Number of substrs containing all three charactors
# Example 1:

# Input: s = "bbacba"
# Output: 9

class Solution:
    def __init__(self, string: str) -> None:
        self.string = string

    def brute_force(self) -> int:
        count = 0
        for i in range(len(self.string)):
            hash = {"a": 0, "b": 0, "c": 0}
            for j in range(i, len(self.string)):
                hash[self.string[j]] = 1
                if hash["a"] + hash["b"] + hash["c"] == 3:
                    count += len(self.string) - j
                    break
                    # OR if dont break then simply increase count by 1
        return count
    
    def optimal(self) -> int:
        count = 0
        last_seen_hash = {"a": -1, "b": -1, "c": -1}
        for right in range(len(self.string)):
            last_seen_hash[self.string[right]] = right
            if last_seen_hash["a"] != -1 and last_seen_hash["b"] != -1 and last_seen_hash["c"] != -1:
                count += min(last_seen_hash["a"], last_seen_hash["b"], last_seen_hash["c"]) + 1
        return count


        
string = "abcabc"
sol = Solution(string)
print(sol.optimal())

        