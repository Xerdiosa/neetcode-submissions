class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = []
        for i in list(s):
            if i.isalnum():
                n.append(i)
        return n == n[::-1]