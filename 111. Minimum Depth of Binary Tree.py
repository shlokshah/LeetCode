class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        if root.left and root.right:
            l=self.minDepth(root.left)
            r=self.minDepth(root.right)
            return min(l,r)+1
        elif root.left==None:
            return self.minDepth(root.right)+1
        else:
            return self.minDepth(root.left)+1
