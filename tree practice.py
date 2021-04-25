class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def insert(root, val):
    if root==None:
        root=TreeNode(val)
        return root
    else:
        if root.val>val:
            root.left=insert(root.left, val)

        else:
            root.right=insert(root.right, val)
    return root

def depth(root):
    if root is None:
        return 0
    else:
        ldepth=depth(root.left)
        rdepth=depth(root.right)
        if ldepth<rdepth:
            return rdepth+1
        else:
            return ldepth+1


def display( root):
    if root:
        display(root.left)
        print(root.val)
        display(root.right)


root=None
root=insert(root, 8)
root=insert(root, 4)
root=insert(root, 12)
root=insert(root, 16)
root=insert(root, 11)
display(root)
print(depth(root))