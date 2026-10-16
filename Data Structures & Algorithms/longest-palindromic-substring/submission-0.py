class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 1
        maxans = s[0]
        def expand(l,r):
            if l<0 or r>=len(s):
                return 0
            if s[l]!=s[r]:
                return 0
            return 2 + expand(l-1,r+1)
        for i in range(1,len(s)):
            cur=1+expand(i-1,i+1)
            if cur>=maxlen:
                maxlen = cur
                width = cur//2
                maxans = s[i-width:i+width+1]
            if s[i]==s[i-1]:
                cur=2+expand(i-2,i+1)
                if cur>=maxlen:
                    maxlen = cur
                    width = (cur//2)-1
                    maxans = s[i-width-1:i+width+1]              
        return maxans
        