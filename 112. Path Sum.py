# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return
        if sum == root.val and root.left == None and root.right == None:
            return True
        sum = sum - root.val
        l = self.hasPathSum(root.left, sum)
        r = self.hasPathSum(root.right, sum)
        return l or r
