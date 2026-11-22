class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        def helper(x,y):
            tmp = 0
            if grid[x][y]==0:
                return 0
            if x==0 or grid[x-1][y]==0:
                tmp+=1
            if x==len(grid)-1 or grid[x+1][y]==0:
                tmp+=1
            if y==0 or grid[x][y-1]==0:
                tmp+=1
            if y==len(grid[0])-1 or grid[x][y+1]==0:
                tmp+=1
            return tmp
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                ans+=helper(x,y)
        return ans