# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next

        if fast == None:
            return head.next
        
        slow_prev = None
        while fast != None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next
        
        slow_prev.next = slow_prev.next.next
        return head