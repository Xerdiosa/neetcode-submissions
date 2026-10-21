class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points)<2:
            return 0
        import heapq
        costheap = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if i==j:
                    pass #shd be impossible, but we can be safe
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                heapq.heappush(costheap, (distance, tuple(points[i]), tuple(points[j])))
        
        runningcost = 0
        heads = dict()

        def find(point):
            og = point
            while heads[point]!=point:
                point=heads[point]
            heads[og]=point
            return point
        def merge(pointA, pointB):
            if find(pointA) != find(pointB):
                heads[find(pointB)]=find(pointA)
    
        while len(costheap)>0:
            distance, pointA, pointB = heapq.heappop(costheap)
            if pointA not in heads:
                heads[pointA] = pointA
            if pointB not in heads:
                heads[pointB] = pointB
            if find(pointA)==find(pointB):
                continue
            merge(pointA,pointB)
            runningcost += distance
        return runningcost
