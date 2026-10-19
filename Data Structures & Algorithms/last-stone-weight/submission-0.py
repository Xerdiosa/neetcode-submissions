class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        pq=[]
        for weight in stones:
            heapq.heappush_max(pq, weight)
        while len(pq)>=2:
            s1 = heapq.heappop_max(pq)
            s2 = heapq.heappop_max(pq)
            if s1==s2:
                continue
            heapq.heappush_max(pq, abs(s1-s2))

        if len(pq)==0:
            return 0
        return pq[0]
