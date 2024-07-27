# You are visiting a farm that has a single row of fruit trees arranged from 
# left to right. The trees are represented by an integer array of arr[], 
# where arr[i]  is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has 
# some strict rules that you must follow :

# You only have two baskets, and each basket can only hold a single type of 
# fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit 
# from every tree (including the start tree) while moving to the right. 
# The picked fruits must fit in one of the baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array of fruits, return the maximum number of fruits you can pick.

# Input: arr[] = [3, 1, 2, 2, 2, 2]
# Output: 5
# Explanation: It's optimal to pick from trees(0-indexed) [1,2,3,4,5]
# i.e, start picking fruit from tree 1.

from typing import List

class Solution:
    def __init__(self, array: List[int]) -> None:
        self.array = array

    def optimal(self) -> int:
        max_len = left = 0
        hash = {}
        for right in range(len(self.array)):
            print(hash)
            if hash.get(self.array[right], None) == None:
                # keep the first appearing index of an item
                hash[self.array[right]] = right
            if len(hash) > 2:
                # Delete the key from hash which was first pushed in hash
                hash.pop(self.array[left])
                # New left index would be first appearance of prev_fruit
                prev_fruit = self.array[right - 1]
                # update the left to first appearance of prev fruit
                left = hash[prev_fruit]
            else:
                # Calculate the max len of subarray
                max_len = max(max_len, right - left + 1)
        return max_len
    
s = Solution([3, 1, 2, 2, 2, 2])
print(s.optimal())