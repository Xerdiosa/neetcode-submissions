# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, ptr = None, head
        while ptr is not None:
            tmp=ptr.next
            ptr.next=prev
            prev = ptr
            ptr = tmp
        return prev