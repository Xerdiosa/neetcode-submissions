class Solution:
    def validPalindrome(self, s: str) -> bool:
        print(len(s))
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                continue
            return self.isPalindrome(s[l+1:r+1]) or self.isPalindrome(s[l:r])
            return False
        return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = []
        for i in list(s):
            if i.isalnum():
                n.append(i)
        return n == n[::-1]