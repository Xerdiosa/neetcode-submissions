# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    import heapq 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, v in enumerate(lists):
            if v is None:
                continue
            heapq.heappush(pq,(v.val,i,v))
        result = None
        head = None
        while len(pq)>0:
            nxt = heapq.heappop(pq)
            i = nxt[1]
            nxt = nxt[2]
            nn = nxt.next
            if result is None:
                result = nxt
                head = result
                # print(result.val)
            else:
                head.next = nxt
                head = head.next
                # print(result.val)
            if nn is None:
                continue
            heapq.heappush(pq,(nn.val,i,nn))            
        return result

        