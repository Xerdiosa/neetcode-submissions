class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]
        zerocount = 0
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        for i in nums:
            if i == 0:
                zerocount = zerocount+1
        if zerocount > 1:
            return [0 for _ in range(len(nums))]
        elif zerocount == 1: # product all
            ret = [0 for _ in range(len(nums))]
            idx = -1
            mul = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    idx = i
                else:
                    mul = mul * nums[i]
            ret[idx] = mul
            return ret
        else:
            ret=[]
            allproduct = 1
            for i in nums:
                allproduct = allproduct * i
            for i in nums:
                ret.append(allproduct//i)
            return ret
        