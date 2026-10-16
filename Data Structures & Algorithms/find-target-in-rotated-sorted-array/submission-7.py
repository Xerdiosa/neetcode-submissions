class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset=self.findMinIdx(nums)
        left = 0
        right = len(nums)-1
        ln = len(nums)
        print(offset)
        while left<right:
            mid=(left+right)//2
            print((left+offset)%ln, (mid+offset)%ln, (right+offset)%ln)
            if nums[(mid+offset)%ln]==target:
                return (mid+offset)%ln
            if nums[(mid+offset)%ln]>target:
                right=mid-1
            else:
                left=mid+1
        if nums[(left+offset)%ln]==target:
            return (left+offset)%ln
        return -1

    def findMinIdx(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[right]<nums[mid]:
                left=mid
            else:
                right=mid
            if nums[mid-1] > nums[mid]:
                return mid
            if nums[(mid+1)%len(nums)] < nums[mid]:
                return (mid+1)%len(nums)
        return 0