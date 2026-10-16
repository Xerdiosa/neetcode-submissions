class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxval = nums[0]
        curval = nums[0]
        for i in range(1,len(nums)):
            curval = max(curval+nums[i],nums[i])
            maxval = max(maxval,curval)
        return maxval
        