# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(r):
            if r is None:
                return True
            if helper(r.left):
                r.left=None
            if helper(r.right):
                r.right=None
            if r.left is None and r.right is None and r.val==target:
                return True
            return False

        if helper(root):
            return None
        return root