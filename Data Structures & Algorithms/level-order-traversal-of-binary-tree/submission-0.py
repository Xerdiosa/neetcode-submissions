# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self._helper(root,0,ans)
        return ans
    
    def _helper(self, root, level, ans):
        if root is None:
            return
        if len(ans)==level:
            ans.append(list())
        ans[level].append(root.val)
        self._helper(root.left, level+1, ans)
        self._helper(root.right, level+1, ans)
        