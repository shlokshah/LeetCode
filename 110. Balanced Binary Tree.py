# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if l>r:
            return l+1
        else:
            return r+1
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        l=self.height(root.left)
        r=self.height(root.right)
        if abs(l-r)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
