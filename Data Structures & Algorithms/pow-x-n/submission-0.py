class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=n*-1
        lst = [1,x]
        tmp = n//2
        while tmp>0:
            lst.append(lst[-1]*lst[-1])
            tmp=tmp//2
        tmp = n
        idx = 1
        ans=1
        while tmp>0:
            if tmp%2==1:
                ans*=lst[idx]
            idx+=1
            tmp=tmp//2
        return ans 
        
        