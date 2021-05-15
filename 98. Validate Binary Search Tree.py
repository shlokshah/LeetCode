# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def help(self, root, r):
        if root:
            self.help(root.left, r)
            r.append(root.val)
            self.help(root.right, r)
    def isValidBST(self, root: TreeNode) -> bool:
        r=[]
        self.help(root, r)
        for i in range(1,len(r)):
            if r[i-1]>=r[i]:
                return False
        return True