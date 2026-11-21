class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        numTrust=[0 for _ in range(n+1)]
        numTrusted=[0 for _ in range(n+1)]
        for t in trust:
            numTrust[t[0]]+=1
            numTrusted[t[1]]+=1
        for i in range(1,n+1):
            if numTrust[i]==0 and numTrusted[i]==n-1:
                return i
        return -1