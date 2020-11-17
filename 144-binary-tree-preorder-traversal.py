# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        #recursion
#         def preorder(root):
#             return [root.val] + preorder(root.left) + preorder(root.right) if root else []

#         return preorder(root)

        stack = []
        inorder = []
        while stack or root:
            if root:
                inorder.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                # inorder.append(node.val)
                root = node.right
        return inorder
