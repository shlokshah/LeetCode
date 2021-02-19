class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.count or index < 0:
            return -1
        if self.head == None:
            return -1
        if index == 0:
            return self.head.val
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head == None:
            new = Node(val)
            new.next = None
            self.head = new
            self.count += 1
        else:
            new = Node(val)
            new.next = self.head
            self.head = new
            self.count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.count or index < 0:
            return None
        elif index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            new = Node(val)
            new.next = cur.next
            cur.next = new
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.count or index < 0:
            return None

        temp = self.head
        if index == 0:
            self.head = temp.next
            self.count -= 1
        else:
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.count -= 1