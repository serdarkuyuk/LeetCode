#     10
#    5  15
#  3 7  x 18
#  L = 7, R = 15
#
#             10
#         5       15
#       3   7    13   18
#     1 x  6 x
# L = 6, R = 10

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



mylist = [10,5,15,3,7,None,18]
# left 2*i+1
# right 2*i+2


def treefunction(mylist, root, i, n):

    if i < n:
        temp = TreeNode(mylist[i])
        root = temp

        root.left = treefunction(mylist, root.left, 2*i+1, n)
        root.righ = treefunction(mylist, root.right, 2*i+2, n)

    return root


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val, end = ' ')
        inOrder(root.right)

n = len(mylist)
root = None
root = treefunction(mylist, root, 0, n)
inOrder(root)
# root = TreeNode(10)
# root.left = TreeNode(5, 3, 7)
# root.right = TreeNode(15, None, 18)
#
#
# print(root.right.left)
