class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>0:
                counter = nums[i]-1
                idx = i+1
                while counter>0 and idx<len(nums):
                    if nums[idx]>=counter:
                        break
                    nums[idx]=counter
                    counter-=1
                    idx+=1
        for i in nums:
            if i == 0:
                return False
        return True