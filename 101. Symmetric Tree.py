# def printLevelOrder(self, root):
#     h = self.height(root)
#     for i in range(1, h + 1):
#         self.printGivenLevel(root, i)
#
#
# def printGivenLevel(self, root, level):
#     if root is None:
#         return
#     if level == 1:
#         print(root.val, end=" ")
#     elif level > 1:
#         self.printGivenLevel(root.left, level - 1)
#         self.printGivenLevel(root.right, level - 1)
#
#
# def height(self, root):
#     if root == None:
#         return 0
#     else:
#         l = self.height(root.left)
#         r = self.height(root.right)
#         if l > r:
#             return l + 1
#         else:
#             return r + 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def ismirror(self, root1, root2):
        if root1 is None and root2==None:
            return True
        if root1 and root2:
            if root1.val==root2.val:
                return self.ismirror(root1.left, root2.right) and self.ismirror(root1.right, root2.left)
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root, root)