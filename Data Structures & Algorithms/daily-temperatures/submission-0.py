class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ln = len(temperatures)-1
        st = list()
        ans = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while len(st)>0 and st[-1][0]<temperatures[i]:
                idx = st.pop()[1]
                ans[idx] = i-idx
            st.append((temperatures[i],i))
        return ans