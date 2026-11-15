class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = dict()
        for word in wordDict:
            ptr = trie
            for char in list(word):
                if char not in ptr:
                    ptr[char]=dict()
                ptr=ptr[char]
            ptr["END"]=word
        ans = []
        tmp = []
        def helper(idx, dct, start):
            if "END" in dct:
                tmp.append(dct["END"])
                helper(idx, trie, True)
                tmp.pop()
            if idx==len(s):
                if start:
                    ans.append(" ".join(tmp))
                return
            if s[idx] not in dct:
                return
            helper(idx+1, dct[s[idx]], False)
        helper(0, trie, True)
        return ans