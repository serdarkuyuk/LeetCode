# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def caller(node, low=float("-inf"), high=float("inf")):

            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return caller(node.left, low, node.val) and caller(node.right, node.val, high)

        return caller(root)


# solution 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]

        while stack:

            root, low, high = stack.pop()

            if not root:
                continue

            value = root.val

            if value <= low or value >= high:
                return False

            stack.append((root.left, low, value))
            stack.append((root.right, value, high))

        return True
