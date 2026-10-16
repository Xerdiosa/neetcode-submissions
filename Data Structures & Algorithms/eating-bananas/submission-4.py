class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left+right)//2
            if self.count(piles,mid)>h:
                left = mid+1
            else:
                right = mid-1
        return right+1

    def count(self, piles: List[int], k: int) -> int:
        total = 0
        for i in piles:
            if i%k == 0:
                total = total+(i//k)
            else:
                total = total+(i//k)+1
        return total