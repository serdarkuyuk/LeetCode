class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, inorder = [], []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inorder.append(root.val)
                root = root.right

        return inorder
