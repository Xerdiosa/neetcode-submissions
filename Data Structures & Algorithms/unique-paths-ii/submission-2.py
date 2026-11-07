class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        ans = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        ans[0][0] = 1
        def helper(x,y):
            if x<0 or y<0 or x>=len(obstacleGrid) or y>=len(obstacleGrid[0]):
                return 0
            if ans[x][y]!=-1:
                return ans[x][y]
            if obstacleGrid[x][y]==1:
                ans[x][y]=0
                return 0
            ans[x][y]=helper(x-1,y)+helper(x,y-1)
            return ans[x][y]
        return helper(len(obstacleGrid)-1, len(obstacleGrid[0])-1)