# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        while ptr != None:
            if ptr.next == ptr:
                return True

            n = ptr.next
            ptr.next = ptr
            ptr = n
        return False