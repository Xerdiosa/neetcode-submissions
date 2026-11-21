class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        dp=dict()
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            ans = 0
            for j in range(1,i):
                ans = max(ans, dp[j]*(i-j), j*(i-j))
            dp[i]=ans
        return dp[n]