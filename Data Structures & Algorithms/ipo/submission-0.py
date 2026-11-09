class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        ready = [] #project that we can do now, maxheap of profits
        too_expensive = [] #project that need more capital, minheap of capita
        for i in range(len(profits)):
            if capital[i]<=w:
                heapq.heappush_max(ready, profits[i])
            else:
                heapq.heappush(too_expensive,(capital[i], profits[i]))
        projectCnt = 0
        while projectCnt<k and len(ready)>0:
            projectCnt+=1
            w+=heapq.heappop_max(ready)
            while len(too_expensive)>0 and too_expensive[0][0]<=w:
                project = heapq.heappop(too_expensive)
                heapq.heappush_max(ready, project[1])
        return w