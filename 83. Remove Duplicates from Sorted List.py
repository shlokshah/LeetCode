# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t1=head
        while (t1 and t1.next):
            if t1.next.val== t1.val:
                t2=t1.next
                t1.next=t2.next
                del t2
            else:
                t1=t1.next
        return head
