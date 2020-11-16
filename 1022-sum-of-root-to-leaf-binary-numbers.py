# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        current_number = 0
        self.leaf_to_total = 0

        def recursion(node, current_number):
            # nonlocal leaf_to_total
            if node:
                current_number = (current_number << 1 | node.val)

                if not node.right and not node.left:
                    self.leaf_to_total += current_number

                recursion(node.left, current_number)
                recursion(node.right, current_number)
        recursion(root, 0)
        return self.leaf_to_total
