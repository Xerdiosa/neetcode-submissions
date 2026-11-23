class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        prev = s[0]
        ans = 0
        for num in s[1:]:
            if dct[prev]<dct[num]:
                ans-=dct[prev]
            else:
                ans+=dct[prev]
            prev=num
        ans+=dct[prev]
        return ans