# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return
        queue=[root]
        result=[]
        while queue:
            count=len(queue)
            temp=[]
            while count>0:
                node=queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count-=1
            result.append(temp)
        return result[::-1]








'''
        result=[]
        queue = []
        j=0
        queue.append(root)
        while (len(queue) > 0):
            temp=[]
        for i in queue[j]:
            node = queue[j]
            temp.append(node.val)
            if node.left and node.right:
                queue.append([node.left, node.right])
            elif node.left:
                queue.append([node.left])
            if node.right:
                queue.append([node.right])
            j+=1
            result.insert(0, temp)
        return result
'''