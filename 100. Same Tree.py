# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def display(self, root):
        q=[]
        if root:
            q.append(root.data)
            self.display(root.left)
            self.display(root.right)
        return q
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p=self.display(p)
        q=self.display(q)
        if p==q:
            return True
        else:
            return False
