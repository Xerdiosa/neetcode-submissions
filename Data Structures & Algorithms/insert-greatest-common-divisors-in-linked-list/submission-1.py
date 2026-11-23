# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return abs(a)
        ptr = head
        while ptr.next is not None:
            gcdVal = gcd(ptr.val, ptr.next.val)
            tmp = ptr.next
            ptr.next = ListNode(val=gcdVal, next=tmp)
            ptr = ptr.next.next
        return head
