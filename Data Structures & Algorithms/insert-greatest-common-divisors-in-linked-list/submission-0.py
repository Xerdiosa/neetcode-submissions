# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        ptr = head
        while ptr.next is not None:
            gcd = math.gcd(ptr.val, ptr.next.val)
            tmp = ptr.next
            ptr.next = ListNode(val=gcd, next=tmp)
            ptr = ptr.next.next
        return head