class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dct = dict()
        for i in nums:
            if i not in dct:
                dct[i]=0
            dct[i]+=1
        for i in range(1000,-1001,-1):
            if i not in dct:
                continue
            if k > dct[i]:
                k-=dct[i]
            else:
                return i
            