class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dct = dict()
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        ans = self.dct[key][0]
        node = self.dct[key][1]
        self.pushBack(node)
        return ans

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct[key][0]=value
            node = self.dct[key][1]
            self.pushBack(node)
            return
        node = Node(key)
        if self.head is None:
            self.head=node
            self.tail=node
        self.dct[key]=[value, node]
        self.pushBack(node)
        if len(self.dct)>self.cap:
            self.removeHead()
        

    def pushBack(self, node):
        if node.key==self.tail.key:
            return
        if node.key==self.head.key and self.head.key!=self.tail.key:
            self.head = node.next
            self.head.prev = None
        node.remove()
        node.prev=self.tail
        self.tail.next = node
        self.tail = self.tail.next

    def removeHead(self):
            head = self.head
            del self.dct[head.key]
            self.head=self.head.next
            self.head.prev=None

class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev
    
    def remove(self):
        prev=self.prev
        next=self.next
        if prev is not None:
            prev.next=next
        if next is not None:
            next.prev=prev