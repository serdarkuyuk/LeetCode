inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        mydict = {item : index for index, item in enumerate(inorder)}

        inorderRange = [0, len(inorder)]
        postorderRange = [0, len(postorder)]

        def helper(inorderRange, postorderRange):

            inorderBegining, inorderEnd = inorderRange
            postorderBegining, postorderEnd = postorderRange

            # base
            if postorderEnd <= postorderBegining:
                return None

            #assigning root
            indice = mydict[postorder[postorderEnd - 1]]
            root = TreeNode(inorder[indice])

            #assing left
            root.left = helper([inorderBegining, indice], [postorderBegining, postorderBegining + indice - inorderBegining])
            #assing right
            root.right = helper([indice+1, inorderEnd], [postorderBegining + indice - inorderBegining, postorderEnd-1])
            return root

        return helper(inorderRange, postorderRange)
