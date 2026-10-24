class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.st = SegmentTreeNodes.build(nums,0,len(nums)-1)
    
    def update(self, index: int, val: int) -> None:
        self.st.update(index,val)
    
    def query(self, L: int, R: int) -> int:
        return self.st.query(L,R)

class SegmentTreeNodes:
    def __init__(self, total, L, R):
        self.total=total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    @staticmethod
    def build(nums, L, R):
        if L==R:
            # print(nums[L],L,R)
            return SegmentTreeNodes(nums[L],L,R)
        root = SegmentTreeNodes(0, L,R)
        M=(L+R)//2
        root.left=SegmentTreeNodes.build(nums,L,M)
        root.right=SegmentTreeNodes.build(nums,M+1,R)
        root.total=root.left.total+root.right.total
        # print(root.total,L,R)
        return root

    def update(self, idx, val):
        if self.L==self.R:
            self.total=val
            return
        M=(self.L+self.R)//2
        if idx<=M:
            self.left.update(idx,val)
        else:
            self.right.update(idx,val)
        self.total = self.left.total + self.right.total
    
    def query(self, L, R):
        if self.L==L and self.R==R:
            return self.total
        M=(self.L+self.R)//2
        if L>M:
            return self.right.query(L,R)
        if R<=M:
            return self.left.query(L,R)
        return self.left.query(L,M) + self.right.query(M+1,R)

        