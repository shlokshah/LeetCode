class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self, root, val):
        if root==None:
            return 0
        val=val*10+root.val
        if root.left==None and root.right==None:
            return val
        return self.check(root.left, val)  + self.check(root.right, val)

    def sumNumbers(self, root: TreeNode) -> int:
        return self.check(root, 0)
