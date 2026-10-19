class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n==1:
            return 0
        import heapq

        # Initialize the queue
        visited=[False for _ in range(n+1)]
        finalcost = [0 for _ in range(n+1)]
        dct = dict()
        pq = []
        for edge in times:
            if edge[0] not in dct:
                dct[edge[0]] = []
            dct[edge[0]].append((edge[2],edge[1]))
        
        def helper(fr,to,cost):
            if visited[to]:
                return
            visited[to]=True
            finalcost[to]=cost
            if to not in dct:
                return
            for edge in dct[to]:
                heapq.heappush(pq, (edge[0]+cost, k, edge[1]))
        
        if k not in dct:
            return -1
        for edge in dct[k]:
            heapq.heappush(pq, (edge[0], k, edge[1]))
        visited[k]=True
        
        while len(pq)>0:
            cost,fr,to=heapq.heappop(pq)
            helper(fr,to,cost)

        ans = 0
        for i in range(1,n+1):
            if not visited[i]:
                return -1
            ans = max(ans,finalcost[i])
        return ans
        