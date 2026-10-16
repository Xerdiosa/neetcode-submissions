class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        occ = dict()
        longest = 1
        startindex = -1
        for i in range(len(s)):
            if s[i] not in occ or startindex > occ[s[i]]:
                occ[s[i]] = i
                if i == len(s)-1:
                    length = i-startindex
                    if length > longest:
                        longest = length    
            else:
                end = i-1
                length = end-startindex
                if length > longest:
                    longest = length
                startindex = occ[s[i]]
                occ[s[i]] = i
        return longest
