# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(val=0, next=None)
        counter = tmp
        while True:
            if list1 is None:
                counter.next = list2
                break
            if list2 is None:
                counter.next = list1
                break
            if list1.val <= list2.val:
                counter.next = list1
                list1 = list1.next
                counter = counter.next
            else:
                counter.next = list2
                list2 = list2.next
                counter = counter.next
        return tmp.next
        
        