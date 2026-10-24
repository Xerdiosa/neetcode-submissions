class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct = dict()
        def getDominant():
            m = 0
            cnt = 0
            mk = None
            for k,v in dct.items():
                if v>m:
                    cnt+=m
                    m=v
                    mk=k
                else:
                    cnt+=v
            return mk, m, cnt
        
        l = 0
        ans=0
        for i in range(len(s)):
            if s[i] in dct:
                dct[s[i]]+=1
            else:
                dct[s[i]]=1
            mk, m, cnt = getDominant()
            # print(mk,m,cnt,dct)
            if cnt>k:
                if dct[s[l]]==1:
                    del dct[s[l]]
                else:
                    dct[s[l]]-=1
                l+=1
            ans = max(i-l+1,ans)
        return ans