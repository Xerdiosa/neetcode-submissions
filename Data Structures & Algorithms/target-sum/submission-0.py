class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=dict()
        def helper(idx, s):
            nonlocal dp
            if (idx,s) in dp:
                return dp[(idx,s)]
            if idx==len(nums):
                if s==target:
                    dp[(idx,s)]=1
                else:
                    dp[(idx,s)]=0
                return dp[(idx,s)]

            dp[(idx,s)]=helper(idx+1, s+nums[idx])+helper(idx+1, s-nums[idx])
            return dp[(idx,s)]
        return helper(0,0)