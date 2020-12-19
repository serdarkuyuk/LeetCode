# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return

        stack = [(root, -math.inf, math.inf)]
        mydict = {}
        while stack:

            root, low, high = stack.pop()

            if not root:
                continue
            value = root.val

            if value < low or value > high:
                return False

            mydict[value] = mydict.get(value, 0) + 1

            stack.append((root.left, low, value))
            stack.append((root.right, value, high))

        c = max(mydict.values())

        return [k for k, v in mydict.items() if v == c]
