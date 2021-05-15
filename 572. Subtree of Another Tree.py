# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, subRoot):
        if root is not None and subRoot is not None:
            if root.val == subRoot.val:
                return self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)
            else:
                return False
        elif (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        else:
            return True

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if self.check(root, subRoot):
            return True
        if root is None:
            return False
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
