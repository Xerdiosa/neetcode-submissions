class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = {}
        for i in range(len(nums)):
            if target-nums[i] in bag:
                return [bag[target-nums[i]],i]
            bag[nums[i]]=i
        return [0,0]
        