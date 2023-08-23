# August-23-2023

# Given a Binary Tree with all unique values and two nodes value, n1 and n2.
# The task is to find the lowest common ancestor of the given two nodes.
# We may assume that either both n1 and n2 are present in the tree or none of them are present.
#
# LCA: It is the first common ancestor of both the nodes n1 and n2 from bottom of tree.
# Input:
# n1 = 2 , n2 = 3
#        1
#       / \
#      2   3
# Output: 1
# Explanation:
# LCA of 2 and 3 is 1.
from typing import Optional


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Solution:
    def __init__(self, n1: TreeNode, n2: TreeNode):
        self.n1 = n1
        self.n2 = n2

    def lca(self, root: TreeNode) -> Optional[TreeNode]:
        if (not root) or (root == self.n1) or (root == self.n2):
            return root

        left = self.lca(root.left)
        right = self.lca(root.right)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root
