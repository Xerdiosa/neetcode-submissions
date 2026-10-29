# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None or head.next.next is None:
            return 
        ptr, second = self.cut(head)
        second=self.reverseList(second)
        while second is not None:
            tmp = ptr.next
            tmp2 = second.next
            ptr.next=second
            ptr.next.next=tmp
            ptr=ptr.next.next
            second=tmp2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, ptr = None, head
        while ptr is not None:
            tmp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = tmp
        return prev

    def ln(self, head: Optional[ListNode]) -> int:
        cnt = 0
        while head is not None:
            cnt+=1
            head = head.next
        return cnt

    def cut(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        first = head
        second = None
        import math
        l = math.ceil(self.ln(head)/2)
        ptr = head
        tmp = None
        for _ in range(l-1):
            tmp = ptr.next.next
            ptr = ptr.next
        ptr.next = None
        return first, tmp