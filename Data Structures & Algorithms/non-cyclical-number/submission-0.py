class Solution:
    def isHappy(self, n: int) -> bool:
        st=set()
        def helper(k):
            if k==1:
                return True
            tmp=0
            while k>0:
                tmp+=(k%10)**2
                k=k//10
            if tmp in st:
                return False
            st.add(tmp)
            return helper(tmp)
        return helper(n)
        