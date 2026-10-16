# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.helper(root.left,root.val,True,None,root.val) and self.helper(root.right,root.val,False,root.val,None)
    def helper(self, root, mid, less, gmn, gmm):
        if root is None:
            return True
        if gmn is not None and root.val<=gmn:
            return False
        if gmm is not None and root.val>=gmm:
            return False
        if less:
            if root.val >= mid:
                return False
        else:
            if root.val <= mid:
                return False
        return self.helper(root.left,root.val,True,gmn,root.val) and self.helper(root.right,root.val,False,root.val,gmm)           
