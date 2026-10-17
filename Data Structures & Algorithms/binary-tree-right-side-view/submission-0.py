# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(r,d):
            if r is None:
                return
            if len(ans)<d:
                ans.append(r.val)
            helper(r.right, d+1)
            helper(r.left, d+1)

        helper(root,1)
        return ans