class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        maxy = len(grid[0])
        maxx = len(grid)
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        islandnum = 0

        def explore(x:int,y:int):
            if x<0 or y<0 or x>=maxx or y>=maxy:
                return
            if visited[x][y]:
                return
            if not grid[x][y] == "1":
                return
            visited[x][y] = True
            explore(x-1,y)
            explore(x+1,y)
            explore(x,y-1)
            explore(x,y+1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and not visited[x][y]:
                    islandnum+=1
                    explore(x,y)
        return islandnum