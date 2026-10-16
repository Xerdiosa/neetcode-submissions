class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[-1 for _ in range(n)] for i in range(m)]
        paths[0][0] = 1
        def helper(mm,nn):
            if nn < 0 or mm < 0:
                return 0
            if paths[mm][nn]==-1:
                paths[mm][nn]=helper(mm-1,nn)+helper(mm,nn-1)
            return paths[mm][nn]
        return helper(m-1,n-1)