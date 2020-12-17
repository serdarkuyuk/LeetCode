# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def caller(node):

            if not node:
                return True, 0

            leftBalanced, leftHeight = caller(node.left)
            rightBalanced, rightHeight = caller(node.right)

            if not leftBalanced:
                return False, 0

            if not rightBalanced:
                return False, 0

            return (abs(leftHeight-rightHeight) < 2), 1 + max(leftHeight, rightHeight)

        return caller(root)[0]
