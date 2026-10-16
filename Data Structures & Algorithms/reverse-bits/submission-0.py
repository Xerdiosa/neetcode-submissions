class Solution:
    def reverseBits(self, n: int) -> int:
        padding = 32
        ans = 0
        while n>0:
            ans = ans | n%2
            if n//2>0:
                ans = ans * 2
            n//=2
            padding-=1
        ans = ans * 2**padding
        return ans