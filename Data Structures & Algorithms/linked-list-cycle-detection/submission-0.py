# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        tortoise = head
        hare = head.next
        while tortoise is not hare:
            if hare.next is None or hare.next.next is None:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
        return True
            
        