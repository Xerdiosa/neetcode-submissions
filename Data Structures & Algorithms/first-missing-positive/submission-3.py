class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in nums[:]:
            if i<=0 or i>=len(nums):
                continue 
            tmp, nums[i-1] = nums[i-1], i
            while tmp>0 and tmp<=len(nums) and tmp!=nums[tmp-1]:
                if nums[tmp-1]>0 and nums[tmp-1]<=len(nums):
                    nums[tmp-1], tmp = tmp, nums[tmp-1]
                else:
                    nums[tmp-1]= tmp
                    break
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1
