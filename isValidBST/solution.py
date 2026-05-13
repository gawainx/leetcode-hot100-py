from leet_chaser.lt_typing import TreeNode
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def validate(self, root: Optional[TreeNode], lower_val, upper_val):
        if lower_val is None and upper_val is None:
            cond = True
        elif lower_val is None:
            cond = root.val < upper_val
        elif upper_val is None:
            cond = lower_val < root.val
        else:
            cond = lower_val < root.val < upper_val

        if root.left is not None:
            cond = cond and self.validate(root.left, lower_val=lower_val, upper_val=root.val)
        if root.right is not None:
            cond = cond and self.validate(root.right, lower_val=root.val, upper_val=upper_val)
        return cond

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.validate(root, None, None)
