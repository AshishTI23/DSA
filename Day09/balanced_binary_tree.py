# August-23-2023

# Given a binary tree, find if it is height balanced or not.
# A tree is height balanced if difference between heights of left and right subtrees is not
# more than one for all nodes of tree.
#
# A height balanced tree
#         1
#      /     \
#    10      39
#   /
# 5
#
# An unbalanced tree
#         1
#      /
#    10
#   /
# 5


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Solution:
    def check_balanced_binary_tree(self, root: TreeNode) -> bool:
        if not root:
            return True

        def balanced(root: TreeNode) -> int:
            if not root:
                return 0
            left = balanced(root.left)
            if left == -1:
                return -1
            right = balanced(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return balanced(root) != -1
