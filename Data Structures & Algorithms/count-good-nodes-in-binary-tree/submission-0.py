# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(r, maxinpath):
            if r is None:
                return 0
            tmp = 0
            if r.val>=maxinpath:
                tmp=1
                maxinpath=r.val
            return tmp++helper(r.left, maxinpath)+helper(r.right,maxinpath)
        return 1+helper(root.left, root.val)+helper(root.right,root.val)
        