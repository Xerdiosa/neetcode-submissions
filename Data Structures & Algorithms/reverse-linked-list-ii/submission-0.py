# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr = head
        prev = None
        for i in range(left-1):
            prev = ptr
            ptr=ptr.next
        p, h = self.reverseList(ptr,right-left+1)
        if prev is None:
            return p
        prev.next = p
        return head

    def reverseList(self, head: Optional[ListNode],k) -> (Optional[ListNode], Optional[ListNode]):
        prev, ptr = None, head
        for _ in range(k):
            tmp=ptr.next
            ptr.next=prev
            prev = ptr
            ptr = tmp
        head.next=ptr
        return prev, head