class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=dict()
        def nextHasStar(pidx):
            if pidx>=len(p)-1:
                return False
            return p[pidx+1]=="*"

        def helper(sidx, pidx):
            print(sidx,pidx)
            if (sidx,pidx) in dp:
                return dp[(sidx,pidx)]
            if sidx>=len(s) and pidx>=len(p):
                dp[(sidx,pidx)]=True
                return dp[(sidx,pidx)]
            if sidx>=len(s) or pidx>=len(p):
                if nextHasStar(pidx):
                    tmp = helper(sidx, pidx+2)
                    if tmp:
                        dp[(sidx,pidx)]=True
                        return True
                dp[(sidx,pidx)]=False
                return dp[(sidx,pidx)]
            #special rule for *
            if nextHasStar(pidx):
                tmp = helper(sidx, pidx+2)
                if tmp:
                    dp[(sidx,pidx)]=True
                    return True

            if s[sidx]!=p[pidx] and p[pidx]!=".":
                dp[(sidx,pidx)]=False
                return dp[(sidx,pidx)]
            if nextHasStar(pidx):
                dp[(sidx,pidx)] = helper(sidx+1, pidx) or helper(sidx+1, pidx+2)
                return dp[(sidx,pidx)]
            dp[(sidx,pidx)] = helper(sidx+1, pidx+1)
            return dp[(sidx,pidx)]
        return helper(0,0)