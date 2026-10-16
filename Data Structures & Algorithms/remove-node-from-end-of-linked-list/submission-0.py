# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tester = head
        count = 1
        while tester.next is not None:
            count +=1
            tester = tester.next
        if count == n:
            return head.next
        if n == 1:
            remover = head
            while remover.next.next is not None:
                remover = remover.next
            remover.next = None
            return head
        remover = head
        for _ in range(count-n-1):
            remover = remover.next
        tmp = remover.next
        remover.next = tmp.next
        return head

        