class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        lastIdx = 1
        for i in range(1,len(nums)):
            if nums[i]==prev:
                pass
            else:
                prev=nums[i]
                nums[lastIdx]=prev
                lastIdx+=1
        for _ in range(len(nums)-lastIdx):
            nums.pop()
        return len(nums)