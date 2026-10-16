class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.hammingWeight(i) for i in range(0,n+1)]
    def hammingWeight(self, n: int) -> int:
        count=0
        while n > 0:
            if n%2 > 0:
                count = count + 1
            n = n//2
        return count