# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        ptr1 = list1
        ptr2 = list2

        if ptr1 == None:
            return ptr2
        elif ptr2 == None:
            return ptr1

        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                selected = ptr1
                ptr1 = ptr1.next
            else:
                selected = ptr2
                ptr2 = ptr2.next
                        
            if head == None:
                head = tail = selected
            else:
                tail.next = selected
                tail = tail.next
        
        if ptr1 != None:
            tail.next = ptr1
        else:
            tail.next = ptr2
        
        return head

