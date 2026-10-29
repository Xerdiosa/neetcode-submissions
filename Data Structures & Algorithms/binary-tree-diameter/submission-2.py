# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        mx = 0
        def maxheight(root, idx):
            nonlocal mx
            if root is None:
                return idx
            left, right= maxheight(root.left,idx+1),maxheight(root.right,idx+1)
            mx = max(mx, (left-idx+right-idx-2))
            return max(left, right)
        mx = max(maxheight(root.left,0)+maxheight(root.right,0), mx)
        return mx
        