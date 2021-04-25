# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            ldepth=self.minDepth(root.left)
            rdepth=self.minDepth(root.right)

            if ldepth>rdepth:
                return rdepth+1
            else:
                return ldepth+1