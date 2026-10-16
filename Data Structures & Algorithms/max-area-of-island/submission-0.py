class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxy = len(grid[0])
        maxx = len(grid)
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxarea = 0

        def explore(x:int,y:int) -> int:
            if x<0 or y<0 or x>=maxx or y>=maxy:
                return 0
            if visited[x][y]:
                return 0 
            if not grid[x][y] == 1:
                return 0
            visited[x][y] = True
            # print(f"visited({x},{y})")
            return 1 + explore(x-1,y) + explore(x+1,y) + explore(x,y-1) + explore(x,y+1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and not visited[x][y]:
                    maxarea = max(maxarea,explore(x,y))
        return maxarea