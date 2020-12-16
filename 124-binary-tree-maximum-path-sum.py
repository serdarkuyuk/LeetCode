# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def caller(node):

            nonlocal maximum
            if not node:
                return 0

            leftGain = max(caller(node.left), 0)
            rightGain = max(caller(node.right), 0)

            total = node.val + rightGain + leftGain

            maximum = max(maximum, total)

            return node.val + max(rightGain, leftGain)

        maximum = float("-inf")
        caller(root)
        return maximum
