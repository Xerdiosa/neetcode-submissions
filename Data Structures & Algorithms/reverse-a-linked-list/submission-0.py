# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        end = None
        ptr = head
        while ptr.next is not None:
            ptr = ptr.next
        self.helper(head, head.next)
        return ptr

    def helper(self, head: Optional[ListNode], next: Optional[ListNode]):
        if next is None:
            return 
        head.next = None
        self.helper(next, next.next)
        next.next = head

