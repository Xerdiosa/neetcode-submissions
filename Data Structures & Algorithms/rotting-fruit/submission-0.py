class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        ans = 0
        def helper(x,y,clock):
            nonlocal ans
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return
            if grid[x][y]==2 or grid[x][y]==0:
                return
            ans=max(clock, ans)
            grid[x][y]=2
            q.append((x+1,y,cost+1))
            q.append((x-1,y,cost+1))
            q.append((x,y+1,cost+1))
            q.append((x,y-1,cost+1))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==2:
                    q.append((x+1,y,1))
                    q.append((x-1,y,1))
                    q.append((x,y+1,1))
                    q.append((x,y-1,1))
        while len(q)>0:
            x,y,cost = q.popleft()
            helper(x,y,cost)
            
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    return -1
        return ans