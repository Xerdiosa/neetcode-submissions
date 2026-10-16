class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[right]<nums[mid]:
                left=mid
            else:
                right=mid
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[(mid+1)%len(nums)] < nums[mid]:
                return nums[(mid+1)%len(nums)]
        # 2021 solution
        # left = 0 
        # right = len(nums) - 1
        # mid = (left + right) / 2
        # while left < right:
        #     if nums[mid] > nums[right]:
        #         left = mid
        #     else:
        #         right = mid
        #     mid = (left + right) / 2
        #     if nums[mid-1] > nums[mid]:
        #         return nums[mid]
        #     if nums[(mid+1)%len(nums)] < nums[mid]:
        #         return nums[(mid+1)%len(nums)]
