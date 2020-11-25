# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:


        def bfs(node, low, high):

            if not node:
                return None

            if node.val < low:
                return bfs(node.right, low, high)

            elif node.val > high:
                return bfs(node.left, low, high)

            else:
                node.left = bfs(node.left, low, high)
                node.right = bfs(node.right, low, high)
                return node

        return bfs(root, low, high)
        
