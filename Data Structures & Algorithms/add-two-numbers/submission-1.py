# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        head = tail = None
        carry = 0
        while p1 != None or p2 != None:
            val = carry
            if p1 != None:
                val += p1.val
            if p2 != None:
                val += p2.val

            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0

            if head == None:
                head = tail = ListNode(val, None)
            else:
                tail.next = ListNode(val, None)
                tail = tail.next

            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
            
        if carry:
            tail.next = ListNode(1, None)

        return head