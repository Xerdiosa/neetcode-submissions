# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        size = self.getSize(root)
        return self.traverse(root, size, k)
    
    def traverse(self, root: Optional[TreeNode], size: Optional[TreeNode], k: int) -> int:
        leftsize = self.getSmaller(size)
        if k==leftsize+1:
            return root.val
        if k<leftsize+1:
            return self.traverse(root.left, size.left, k)
        if k>leftsize+1:
            return self.traverse(root.right, size.right, k-leftsize-1)

    def getSmaller(self, size: Optional[TreeNode]) -> int:
        if size.left is None:
            return 0
        return size.left.val

    def getSize(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        t = TreeNode(1, self.getSize(root.left), self.getSize(root.right))
        if t.right is not None:
            t.val = t.val + t.right.val
        if t.left is not None:
            t.val = t.val + t.left.val
        return t
