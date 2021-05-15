# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return
        if root.val == p.val or root.val == q.val:
            return root

        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)

        if L and R:
            return root

        if L is not None and R is None:
            return L
        else:
            return R
