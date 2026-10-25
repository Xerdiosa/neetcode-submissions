# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ln(head):
            ptr=0
            while head is not None:
                ptr+=1
                head=head.next
            return ptr

        def get(head):
            if head is None:
                return 0
            return head.val

        if ln(l1)<ln(l2):
            l1,l2 = l2,l1
        l1h = l1
        l2h = l2
        borrow = 0
        while l1h is not None or l2h is not None:
            tmp = get(l1h)+get(l2h)+borrow
            borrow = tmp//10
            l1h.val=tmp%10
            if l1h.next is None and borrow>0:
                l1h.next = ListNode(val=0, next=None)
            l1h = l1h.next
            l2h = l2h.next if l2h is not None else None
        return l1
        