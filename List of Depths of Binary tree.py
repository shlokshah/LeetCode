class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class Tree:
    def insert(self, root, val):
        if root is None:
            root=TreeNode(val)
            return root
        else:
            if root.val>=val:
                root.left=self.insert(root.left, val)
                # print('inserted ', val)
            else:
                root.right=self.insert(root.right, val)
                # print('inserted ', val)
            return root

    def display(self, root):
        if root:
            self.display(root.left)
            print(root.val)
            self.display(root.right)

    def ListDepth(self, root):
        if root is None:
            return []
        Q=[[root]]
        final=[[root]]
        while len(Q)>0:
            top=Q.pop(0)
            temp=[]
            for i in top:
                if i.left!=None:
                    temp.append(i.left)
                if i.right!=None:
                    temp.append(i.right)
            if len(temp)>0:
                final.append(temp)
                Q.append(temp)
        return final

def makelist(final):
    result=[]
    for level in final:
        head=None
        tail=None
        for node in level:
            if head==None:
                head=tail=Node(node.val)
            else:
                temp=Node(node.val)
                tail.next=temp
                tail=temp
        result.append(head)
    for i in result:
        head=i
        while head!=None:
            print(head.val,end="->")
            head=head.next
        print()

if __name__ == '__main__':
    root=None
    T=Tree()
    for i in [8,4,12,2,6,13,5,7]:
        root = T.insert(root, i)
    # T.display(root)
    final=T.ListDepth(root)
    for i in final:
        for j in i:
            print(j.val, end=" ")
        print()
    makelist(final)