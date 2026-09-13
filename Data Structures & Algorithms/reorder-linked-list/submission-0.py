# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cnt = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            cnt += 1
        
        cnt_left = cnt - cnt // 2
        ptr = head
        cnt = 0
        while cnt < cnt_left - 1:
            cnt += 1
            ptr = ptr.next

        n = ptr.next
        ptr.next = None
        ptr = n
        # print(ptr.val)

        # reverse
        prev = None
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
        

        