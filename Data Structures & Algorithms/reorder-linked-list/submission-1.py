# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        slow_prev = None
        fast_prev = None

        while fast:
            slow_prev = slow
            slow = slow.next
            if fast.next:
                fast_prev = fast.next
                fast = fast.next.next
            else:
                fast_prev = fast
                fast = fast.next

        # reverse
        prev = None
        ptr = slow
        slow_prev.next = None
        while ptr != None:
            n = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = n
        # print(prev.val, prev.next.val)

        ptr1 = head
        ptr2 = prev

        while ptr1 != None and ptr2 != None:
            p1_next = ptr1.next
            p2_next = ptr2.next

            ptr1.next = ptr2
            ptr2.next = p1_next

            ptr1 = p1_next
            ptr2 = p2_next
        

        