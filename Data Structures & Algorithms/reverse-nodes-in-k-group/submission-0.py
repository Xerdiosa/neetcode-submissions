# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if self.ln(head,k)<k:
            return head
        ans, nxt = self.reverseList(head,k)
        while self.ln(nxt.next,k)>=k:
            tmp = nxt
            nh, nxt = self.reverseList(nxt.next,k)
            tmp.next=nh
        return ans 

    def ln(self, head: Optional[ListNode], k)->int:
        if head is None:
            return 0
        counter = 0
        while head is not None:
            counter+=1
            head=head.next
            if counter==k:
                return counter
        return counter

    def reverseList(self, head: Optional[ListNode],k) -> (Optional[ListNode], Optional[ListNode]):
        prev, ptr = None, head
        for _ in range(k):
            tmp=ptr.next
            ptr.next=prev
            prev = ptr
            ptr = tmp
        head.next=ptr
        return prev, head