"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        ptr = head
        while ptr != None:
            ptr.next = Node(ptr.val, ptr.next, ptr.random)
            ptr = ptr.next.next
        
        ptr = head.next
        while ptr != None:
            if ptr.random != None:
                ptr.random = ptr.random.next
            if ptr.next != None:
                ptr = ptr.next.next
            else:
                break

        ptr1 = head1 = head
        ptr2 = head2 = head.next
        while ptr2 != None:
            ptr1.next = ptr1.next.next
            if ptr2.next != None:
                ptr2.next = ptr2.next.next

            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return head2