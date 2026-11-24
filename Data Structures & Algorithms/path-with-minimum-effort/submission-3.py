class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq
        pq = []
        visited = set()
        ans = -1
        def helper(x,y,curcost):
            nonlocal ans
            if ans != -1:
                return
            if (x,y) in visited:
                return
            if x==len(heights)-1 and y==len(heights[0])-1:
                ans = curcost
                return
            visited.add((x,y))
            if x>0:
                heapq.heappush(pq,(max(curcost,abs(heights[x][y]-heights[x-1][y])),x-1,y))
            if y>0:
                heapq.heappush(pq,(max(curcost,abs(heights[x][y]-heights[x][y-1])),x,y-1))
            if x+1<len(heights):
                heapq.heappush(pq,(max(curcost,abs(heights[x][y]-heights[x+1][y])),x+1,y))
            if y+1<len(heights[0]):
                heapq.heappush(pq,(max(curcost,abs(heights[x][y]-heights[x][y+1])),x,y+1))
        heapq.heappush(pq, (0,0,0))
        while len(pq)>0:
            nxt = heapq.heappop(pq)
            helper(nxt[1], nxt[2], nxt[0])
        return ans