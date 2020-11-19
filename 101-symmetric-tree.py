class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def isMirror(tree1, tree2):
            if not tree1 or not tree2: # if one of them is null
                return tree2 == tree1  # compare them
            if tree1.val != tree2.val: # if above not executed, means they are both number
                return False           # if they are both different return false
                                       # if they are similar go and look further
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)

        return isMirror(root.left, root.right)


class Solution:
    def isSymmetric(self, root):
        stack = []
        if root:
            stack.append([root.left, root.right])
        else:
            return True

        while stack:
            tree1, tree2 = stack.pop()

            if tree1 and tree2:
                if tree1.val != tree2.val:
                    return False
                stack.append([tree1.left, tree2.right])
                stack.append([tree1.right, tree2.left])

            elif tree1 or tree2:
                return False

        return True
