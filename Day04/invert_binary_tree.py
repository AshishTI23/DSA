# August-20-2023

# Given the root of a binary tree, invert the tree, and return its root

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_binary_tree_with_recursion(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        return root
