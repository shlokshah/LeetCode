'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1=l1
        one=""
        while cur1!=None:
            one=one+str(cur1.val)
            cur1=cur1.next
        one=one[::-1]
        one=int(one)
        print(one)
        cur2 = l2
        two = ""
        while cur2 != None:
            two = two + str(cur2.val)
            cur2 = cur2.next
        two = two[::-1]
        two = int(two)
        print(two)
        sum=str(one+two)
        sum=sum[::-1]
        start=None
        for i in sum:
            A=ListNode(i)
            if start==None:
                A.next=None
                start=A
            else:
                A.next=start
                start=A
        return start

A=Solution()
l2=ListNode(2)
l4=ListNode(4)
l2.next=l4
l3=ListNode(3)
l5=ListNode(5)
l3.next=l5
print(A.addTwoNumbers(l2,l3))