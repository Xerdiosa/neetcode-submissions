class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        for i in range(len(nums)):
            if maxjump>=len(nums)-1:
                return True
            if i>maxjump:
                return False
            maxjump = max(maxjump, i+nums[i])
        return False