if not t1:
    return t2
elif not t2:
    return t1
else:
    res = TreeNode(t1.val+t2.val)
    res.left = self.mergeTrees(t1.left, t2.left)
    res.right = self.mergeTrees(t1.right, t2.right)
return res
