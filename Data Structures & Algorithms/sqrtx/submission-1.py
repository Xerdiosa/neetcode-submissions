class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1:
            return 1
        l = 1
        r = x
        while l<=r:
            mid = (l+r)//2
            p = mid*mid
            if p==x:
                return mid
            if p>x:
                r = mid-1
            else:
                l = mid+1
        return r