class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sanagram = [0 for i in range(26)]
        tanagram = [0 for i in range(26)]
        for i in list(s):
            sanagram[ord(i)-97]=sanagram[ord(i)-97]+1
        for i in list(t):
            tanagram[ord(i)-97]=tanagram[ord(i)-97]+1
        for i in range(26):
            if sanagram[i] != tanagram[i]:
                return False
        return True