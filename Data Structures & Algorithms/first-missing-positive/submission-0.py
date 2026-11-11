class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        for i in nums[:]:
            # print()
            whilecounter=0
            if i<=0 or i>=len(nums):
                continue 
            tmp, nums[i] = nums[i], i
            while tmp>0 and tmp<=len(nums)-1 and tmp!=nums[tmp] and whilecounter<5:
                whilecounter+=1
                if nums[tmp]>0 and nums[tmp]<=len(nums)-1:
                    # print(tmp, nums)
                    nums[tmp], tmp = tmp, nums[tmp]
                else:
                    nums[tmp]= tmp
                    break
        # print(nums)
        for i in range(1,len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)
