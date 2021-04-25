class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Tree:
    def insert(self, root, val):
        if root is None:
            root=Node(val)
            return root
        else:
            if root.val>=val:
                root.left=self.insert(root.left, val)
            else:
                root.right=self.insert(root.right, val)
            return root

    def display(self, root):
        if root:
            self.display(root.left)
            print(root.val)
            self.display(root.right)

    def depth(self, root):
        if root is None:
            return 0
        else:
            ldepth=self.depth(root.left)
            rdepth=self.depth(root.right)

            if ldepth<rdepth:
                return ldepth+1
            else:
                return rdepth+1
T=Tree()
root=None

def split(L, root, T):
    n=len(L)
    if n>2:
        mid=int(n/2)
        root=T.insert(root, L[mid])
        print(L[mid], "inserted")
        split(L[0:mid], root, T)
        split(L[mid+1:n], root, T)
        return root
    if 0<n<=2:
        for i in range(n):
            root=T.insert(root, L[i])
            print(L[i], 'Inserted')
            return root
    else:
        return

l=[1,2,3,4,5]
root=split(l, root, T)
T.display(root)
print('Min Depth: ',T.depth(root))