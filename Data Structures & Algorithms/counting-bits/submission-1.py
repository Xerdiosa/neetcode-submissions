class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n==1:
            return [0,1]
        if n==2:
            return [0,1,1]

        ans = [0 for _ in range(n+1)]
        ans[1] = 1
        offset = 1
        for i in range(2,len(ans)):
            if i==offset*2:
                ans[i]=1
                offset = i
                continue
            ans[i] = 1+ans[i-offset]
        return ans