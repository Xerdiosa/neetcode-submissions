# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(r):
            if r is None:
                return True, 0
            lb, rb = helper(r.left), helper(r.right)
            return abs(lb[1]-rb[1])<=1 and lb[0] and rb[0], max(lb[1],rb[1])+1
        ans, _ = helper(root)
        return ans