class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=1
        def expand(l,r):
            if l<0 or r>=len(s):
                return 0
            if s[l]!=s[r]:
                return 0
            return 1 + expand(l-1,r+1)
        for i in range(1,len(s)):
            ans+=1+expand(i-1,i+1)
            if s[i]==s[i-1]:
                ans+=1+expand(i-2,i+1)            
        return ans