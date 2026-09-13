# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def printNode(ptr):
    if ptr == None:
        return 'None'
    elif ptr.next == None:
        return f'{ptr.val} None'
    else:
        return f'{ptr.val} {ptr.next.val}'

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        l = dummy
        r = dummy

        while r != None:
            for i in range(0, k):
                r = r.next
                if r == None:
                    break

            if r == None:
                break

            prev = r.next
            ptr = l.next
            stop = r.next

            while ptr != stop:
                _next = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = _next

            _next = l.next
            l.next = r
            l = r = _next

        return dummy.next


            

