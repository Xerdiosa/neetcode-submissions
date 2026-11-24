# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def get1(r):
            ans = 0
            ans += r.left.val if r.left is not None else 0
            ans += r.right.val if r.right is not None else 0
            return ans
        def get2(r):
            ans = 0
            if r.right is not None:
                tmp = r.right
                ans += tmp.left.val if tmp.left is not None else 0
                ans += tmp.right.val if tmp.right is not None else 0
            if r.left is not None:
                tmp = r.left
                ans += tmp.left.val if tmp.left is not None else 0
                ans += tmp.right.val if tmp.right is not None else 0
            return ans
        def helper(r):
            if r is None:
                return None
            if r.left is None and r.right is None:
                return TreeNode(r.val)
            dp = TreeNode(0, helper(r.left), helper(r.right))
            dp.val = max(r.val+get2(dp),get1(dp))
            return dp
        dp = helper(root)
        return dp.val