class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = dict()
        trie = dict()
        for string in dictionary:
            ptr = trie
            for char in list(string):
                if char not in ptr:
                    ptr[char]=dict()
                ptr = ptr[char]
            ptr["end"]=len(string)
        def helper(idx):
            nonlocal dp
            ans = len(s)-idx
            if idx in dp:
                return dp[idx]
            ptr = trie
            ptrIdx = idx
            while True:
                if "end" in ptr:
                    ans = min(ans, helper(idx+ptr["end"]))
                if ptrIdx>=len(s):
                    break
                if s[ptrIdx] in ptr:
                    ptr = ptr[s[ptrIdx]]
                    ptrIdx+=1
                else:
                    break
            if idx+1<len(s):
                print(idx, ans, 1+helper(idx+1))
                ans = min(ans, 1+helper(idx+1))
            dp[idx]=ans
            return ans
        helper(0)
        # print(dp)
        return helper(0)