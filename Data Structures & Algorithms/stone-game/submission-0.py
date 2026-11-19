class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = dict()
        ps = []
        ps.append(piles[0])
        for i in piles[1:]:
            ps.append(ps[-1]+i)
        def helper(x,y):
            if (x,y) in dp:
                return dp[(x,y)]
            if y-x==1:
                dp[(x,y)]=piles[x]
                return dp[(x,y)]
            dp[(x,y)] = max(
                # 1 2 3 1
                # 1 3 6 7
                piles[x]+(ps[y-1]-ps[x]-helper(x+1,y)),
                piles[y-1]+(ps[y-2]-(ps[x-1] if x>0 else 0)-helper(x,y-1))
            )
            return dp[(x,y)]
        return helper(0,len(piles)) > ps[-1]//2
        