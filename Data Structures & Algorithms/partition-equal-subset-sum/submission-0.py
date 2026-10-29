class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if total%2==1:
            return False
        target = total//2


        from functools import cache
        @cache
        def helper(i,s):
            if s==target:
                return True
            if s>target:
                return False
            if i==len(nums):
                return False
            return helper(i+1, s) or helper(i+1, s+nums[i])

        return helper(0,0)