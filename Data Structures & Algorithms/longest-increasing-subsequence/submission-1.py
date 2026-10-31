class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1 for _ in range(len(nums))]
        ans = 1
        for i in range(1,len(nums)):
            tmp = 0
            for j in range(i):
                if nums[i]<=nums[j]:
                    continue
                tmp = max(tmp, dp[j])
            dp[i]=1+tmp
            ans=max(ans,dp[i])
        return ans
