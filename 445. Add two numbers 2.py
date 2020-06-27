'''You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def test(self):
        pass
    def addTwoNumbers(self, l1, l2):
        n1=0
        while l1!= None:
            n1 *= 10
            n1+=l1.val
            l1=l1.next
        n2 = 0
        while l2 != None:
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        print(n2)
        n1=n1+n2
        n1=str(n1)
        start=None
        for i in n1:
            l=ListNode(int(i))
            if start==None:
                l.next=None
                start=l
            else:
                l.next=start
                start=l
        # return start



A=Solution()
l1=ListNode(5)
l2=ListNode(6)
l3=ListNode(4)
l1.next=l2
l2.next=l3
l4=ListNode(7)
l5=ListNode(2)
l6=ListNode(4)
l7=ListNode(3)
l4.next=l5
l5.next=l6
l6.next=l7
print(A.addTwoNumbers(l1,l4))