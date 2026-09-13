class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def _preempt(self):
        if self.tail == None:
            assert self.head == None
            return
        else:
            self.map.pop(self.tail.key)
            if self.head == self.tail:
                # only node, just remove
                assert self.head.prev == None
                assert self.tail.next == None
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def _move_to_head(self, node):
        if self.tail == self.head:
            # only one node, nothing needed
            return
        else:
            if node != self.head:
                node.prev.next = node.next
            else:
                self.head = node.next

            if node != self.tail:
                node.next.prev = node.prev
            else:
                self.tail = node.prev

            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    def get(self, key: int) -> int:
        if self.map.get(key, None) == None:
            return -1
        else:
            node = self.map[key]
            self._move_to_head(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_head(node)
            return
        
        if len(self.map) == self.capacity:
            self._preempt()
        
        node = Node(key, value, None, None)
        self.map[key] = node

        if self.head == None:
            assert self.tail == None
            self.head = self.tail = node
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
        
            

        
