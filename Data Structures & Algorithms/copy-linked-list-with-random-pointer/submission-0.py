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
        if head is None:
            return None
        dct = dict()
        ptr = head
        while True:
            if ptr is None:
                break
            dct[id(ptr)]=(ptr, Node(ptr.val))
            ptr = ptr.next
        ptr = head
        while True:
            if ptr is None:
                break
            if ptr.next is not None:
                dct[id(ptr)][1].next=dct[id(ptr.next)][1]
            if ptr.random is not None:
                dct[id(ptr)][1].random=dct[id(ptr.random)][1]
            ptr = ptr.next
        return dct[id(head)][1]
        