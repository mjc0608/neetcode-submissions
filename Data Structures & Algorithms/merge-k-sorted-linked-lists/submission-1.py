# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop
from itertools import count

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = None
        ptr = None
        breaker = count()

        for i in range(0, len(lists)):
            if lists[i] != None:
                heappush(heap, (lists[i].val, next(breaker), lists[i]))
                lists[i] = lists[i].next

        head = ptr = None
        while len(heap) > 0:
            val, _, node = heappop(heap)
            if node.next != None:
                heappush(heap, (node.next.val, next(breaker), node.next))
        
            if head == None:
                head = ptr = node
            else:
                ptr.next = node
                ptr = ptr.next
                    
        return head

        
