class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        costs = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        costs[0][0] = 0
        import heapq
        pq = []
        def checkbound(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return False
            return True
        def helper(x,y,cost):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return
            if costs[x][y] is not None:
                return
            costs[x][y]=cost
            if checkbound(x+1,y):
                heapq.heappush(pq, (max(cost,grid[x+1][y]),x+1,y))
            if checkbound(x-1,y):
                heapq.heappush(pq, (max(cost,grid[x-1][y]),x-1,y))
            if checkbound(x,y+1):
                heapq.heappush(pq, (max(cost,grid[x][y+1]),x,y+1))
            if checkbound(x,y-1):
                heapq.heappush(pq, (max(cost,grid[x][y-1]),x,y-1))
        if checkbound(0,1):
            heapq.heappush(pq, (max(grid[0][0],grid[0][1]),0,1))
        if checkbound(1,0):
            heapq.heappush(pq, (max(grid[0][0],grid[1][0]),1,0))
        while len(pq)>0:
            path = heapq.heappop(pq)
            helper(path[1],path[2],path[0])
        print(costs)
        return costs[len(grid)-1][len(grid[0])-1]
        