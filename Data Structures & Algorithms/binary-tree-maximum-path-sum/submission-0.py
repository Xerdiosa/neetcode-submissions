# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -10000
        def helper(r):
            nonlocal ans
            if r is None:
                return None
            newRoot = TreeNode(0, helper(r.left), helper(r.right))
            leftval = max(newRoot.left.val if newRoot.left is not None else 0, 0)
            rightval = max(newRoot.right.val if newRoot.right is not None else 0, 0)
            ans = max(ans, r.val+leftval+rightval)
            newRoot.val=max(leftval,rightval)+r.val
            return newRoot
        dp = helper(root) #dp represent maxpath(single path)
        return ans