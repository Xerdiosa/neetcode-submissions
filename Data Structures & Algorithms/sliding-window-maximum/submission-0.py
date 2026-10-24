class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        st = SegmentTreeNodes.build(nums)
        for i in range(len(nums)-k+1):
            ans.append(st.query(i,i+k-1))
        return ans

class SegmentTreeNodes:
    def __init__(self, mx, L, R):
        self.mx=mx
        self.left = None
        self.right = None
        self.L = L
        self.R = R
    
    @staticmethod
    def build(nums):
        return SegmentTreeNodes.__build(nums,0,len(nums)-1)

    @staticmethod
    def __build(nums, L, R):
        if L==R:
            return SegmentTreeNodes(nums[L],L,R)
        root = SegmentTreeNodes(-10001, L,R) #minimum value based on the constraint
        M=(L+R)//2
        root.left=SegmentTreeNodes.__build(nums,L,M)
        root.right=SegmentTreeNodes.__build(nums,M+1,R)
        root.mx=max(root.left.mx,root.right.mx)
        return root

    def update(self, idx, val):
        if self.L==self.R:
            self.mx=val
            return
        M=(self.L+self.R)//2
        if idx<=M:
            self.left.update(idx,val)
        else:
            self.right.update(idx,val)
        self.mx = max(self.left.mx, self.right.mx)
    
    def query(self, L, R):
        if self.L==L and self.R==R:
            return self.mx
        M=(self.L+self.R)//2
        if L>M:
            return self.right.query(L,R)
        if R<=M:
            return self.left.query(L,R)
        return max(self.left.query(L,M), self.right.query(M+1,R))