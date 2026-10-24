class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)==1:
            return s if s==t else ""
        subs=dict()
        tdict=dict()
        for i in t:
            if i not in tdict:
                tdict[i]=1
            else:
                tdict[i]+=1
        ans = ""
        def valid() -> bool:
            for tchar in tdict:
                if subs.get(tchar,0)<tdict[tchar]:
                    return False
            return True
        l=0
        for i in range(len(s)):
            if s[i] not in subs:
                subs[s[i]]=1
            else:
                subs[s[i]]+=1
            if valid():
                while s[l] not in tdict or subs[s[l]]>tdict[s[l]]:
                    subs[s[l]]-=1
                    l+=1
                if ans=="" or len(ans)>i-l+1:
                    ans=s[l:i+1]
        
        return ans