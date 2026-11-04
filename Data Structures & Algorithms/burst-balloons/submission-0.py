class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = dict()
        def helper(n):
            if len(n)==0:
                return 0
            if tuple(n) in dp:
                return dp[tuple(n)]
            ans = 0
            for i in range(len(n)):
                tmp = n[i-1] if i>0 else 1
                tmp *= n[i]
                tmp *= n[i+1] if i<=len(n)-2 else 1
                val = n[i]
                n.pop(i)
                tmp+=helper(n)
                n.insert(i,val)
                ans = max(ans,tmp)
            dp[tuple(n)]=ans
            return ans
        ans= helper(nums)
        print(dp)
        return ans