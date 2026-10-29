class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if total%2==1:
            return False
        target = total//2

        dct=dict()

        def helper(i,s):
            nonlocal dct
            if (i,s) in dct:
                return dct[(i,s)]
            if s==target:
                dct[(i,s)]=True
                return True
            if s>target:
                dct[(i,s)]=False
                return False
            if i==len(nums):
                dct[(i,s)]=False
                return False
            dct[(i,s)] = helper(i+1, s) or helper(i+1, s+nums[i])
            return dct[(i,s)]

        return helper(0,0)