class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        maxcount = 0
        for i in nums:
            st.add(i)
        for i in nums:
            if i-1 in st:
                continue
            curcount = 0
            j = i
            while j in st:
                if j in st:
                    curcount = curcount + 1
                j = j + 1
            if maxcount < curcount:
                maxcount = curcount
        return maxcount 
            