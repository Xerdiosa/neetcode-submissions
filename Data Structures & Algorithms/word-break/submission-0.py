class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [-1 for _ in range(len(list(s))+5)]
        def helper(ss):
            if len(ss)==0:
                dp[0]=1
                return 1
            if dp[len(ss)]>=0:
                return dp[len(ss)] 
            for word in wordDict:
                if ss.startswith(word):
                    if helper(ss[len(word):])==1:
                        dp[len(ss)]=1
                        return 1
            dp[len(ss)]=0
            return 0
        helper(s)
        return True if dp[len(list(s))]==1 else False
