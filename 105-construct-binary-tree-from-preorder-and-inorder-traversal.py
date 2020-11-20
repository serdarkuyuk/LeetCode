# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mydict = {item : index for index, item in enumerate(inorder)}

        inorderRange = [0, len(inorder)]
        preorderRange = [0, len(preorder)]

        def helper(inorderRange, preorderRange):
            inorderBegining, inorderEnding = inorderRange
            preorderBegining, preorderEnding = preorderRange

            #base
            if preorderEnding <= preorderBegining:
                return None


            indice = mydict[preorder[preorderBegining]]
            # print(indice)
            root = TreeNode(inorder[indice])

            root.left = helper([inorderBegining, indice],[preorderBegining+1, preorderBegining+1 + indice - inorderBegining])
            root.right = helper([indice+1, inorderEnding],[preorderBegining+1 + indice - inorderBegining, preorderEnding])
            return root

        return helper(inorderRange, preorderRange)
