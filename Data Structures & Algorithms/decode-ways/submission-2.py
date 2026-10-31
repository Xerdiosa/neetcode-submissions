class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        if len(s)==1:
            return 1

        def canOne(idx):
            if s[idx]!="0":
                return True
        def canTwo(idx): #must not be on first index
            if s[idx-1]=="0":
                return False
            return int(s[idx-1])*10+int(s[idx])<=26
        ans = [0 for _ in range(len(s))]
        ans[0]=1 # 0 already covered in first line
        ans[1]=0
        if canTwo(1):
            ans[1]+=1
        if canOne(1):
            ans[1]+=1
        for i in range(2,len(s)):
            tmp = 0
            if canOne(i):
                tmp+=ans[i-1]
            if canTwo(i):
                tmp+=ans[i-2]
            ans[i]=tmp
        return ans[-1]
    