class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1
        total = len(nums1)+len(nums2)
        half = total//2
        l=0
        r=len(nums1)-1
        while True:
            mid = (l+r)//2
            pivot = half-mid-2
            num1l = nums1[mid] if mid>=0 else -10000000
            num1r = nums1[mid+1] if mid+1<len(nums1) else 10000000
            num2l = nums2[pivot] if pivot>=0 else -10000000
            num2r = nums2[pivot+1] if pivot+1<len(nums2) else 10000000
            if num1l<=num2r and num2l<=num1r:
                if total%2==0:
                    return (max(num1l,num2l)+min(num1r,num2r))/2
                return min(num1r,num2r)
            if num1l>num2r:
                r = mid-1
            else:
                l = mid+1