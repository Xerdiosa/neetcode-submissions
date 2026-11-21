class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        import heapq
        pq = []
        for t in trips:
            heapq.heappush(pq, (t[1],t[0]))
            heapq.heappush(pq, (t[2],-t[0]))
        occ=0
        while len(pq)>0:
            p = heapq.heappop(pq)
            occ+=p[1]
            while len(pq)>0 and p[0]==pq[0][0]:
                n = heapq.heappop(pq)
                occ+=n[1]
            if occ>capacity:
                return False
        return True