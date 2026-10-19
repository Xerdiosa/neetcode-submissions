class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        # Initialize the queue
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = deque()
        def helper(x,y,cost):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return
            if visited[x][y]:
                return
            if grid[x][y]==-1:
                return
            if grid[x][y]<cost:
                return
            visited[x][y]=True
            grid[x][y]=cost
            queue.append((x+1,y,cost+1))
            queue.append((x-1,y,cost+1))
            queue.append((x,y+1,cost+1))
            queue.append((x,y-1,cost+1))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==0:
                    queue.append((x,y,0))
        while len(queue)>0:
            x,y,cost=queue.popleft()
            helper(x,y,cost)
        