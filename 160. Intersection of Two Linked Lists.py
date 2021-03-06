# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return
        LastA = headA
        LastB = headB
        nA = nB = 1
        while (LastA.next != None):
            LastA = LastA.next
            nA += 1
        while (LastB.next != None):
            LastB = LastB.next
            nB += 1
        if LastA != LastB:
            return None
        else:
            LastA = headA
            LastB = headB
            if nA > nB:
                for _ in range(nA - nB):
                    LastA = LastA.next
            elif nA < nB:
                for _ in range(nB - nA):
                    LastB = LastB.next
            while LastA != LastB:
                LastA = LastA.next
                LastB = LastB.next
            return LastA

