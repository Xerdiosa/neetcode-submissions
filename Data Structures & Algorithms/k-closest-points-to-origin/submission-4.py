class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        pq = []
        ans = []
        for point in points:
            dist = ((point[0]**2) + (point[1]**2))**0.5
            heapq.heappush(pq, (dist, point[:]))
        for _ in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans
        