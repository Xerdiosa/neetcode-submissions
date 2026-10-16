class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxval = nums[0]
        curval = nums[0]
        curvalmin = nums[0]
        for i in range(1,len(nums)):
            prevcurval = curval
            prevcurvalmin = curvalmin
            curval = max(prevcurval*nums[i],prevcurvalmin*nums[i],nums[i])
            curvalmin = min(prevcurval*nums[i],prevcurvalmin*nums[i],nums[i])
            maxval = max(maxval,curval)
        return maxval   