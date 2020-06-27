# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        h1 = l1
        h2 = l2
        h3 = ListNode(None)
        temp = h3
        while (h1 != None or h2 != None):
            if (h1 and h2):
                if (h1.val <= h2.val):
                    h3.next = ListNode(h1.val)
                    h3 = h3.next
                    h1 = h1.next
                else:
                    h3.next = ListNode(h2.val)
                    h3 = h3.next
                    h2 = h2.next
            elif h1:
                h3.next = ListNode(h1.val)
                h3 = h3.next
                h1 = h1.next
            else:
                h3.next = ListNode(h2.val)
                h3 = h3.next
                h2 = h2.next
        temp = temp.next
        return temp




