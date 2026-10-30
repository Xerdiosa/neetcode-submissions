class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        def smaller(x1,y1,x2,y2):
            if x1<0 or y1<0 or x1>=len(matrix) or y1>=len(matrix[0]):
                return False
            if x2<0 or y2<0 or x2>=len(matrix) or y2>=len(matrix[0]):
                return False
            return matrix[x2][y2]<matrix[x1][y1]

        def helper(x,y):
            if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]):
                return 0
            if dp[x][y]!=-1:
                return dp[x][y]
            up = helper(x-1,y) if smaller(x,y,x-1,y) else 0
            down = helper(x+1,y) if smaller(x,y,x+1,y) else 0
            left = helper(x,y-1) if smaller(x,y,x,y-1) else 0
            right = helper(x,y+1) if smaller(x,y,x,y+1) else 0
            dp[x][y] = 1+max(up,down,left,right)
            return dp[x][y]
        ans = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                ans = max(ans, helper(x,y))
        return ans