# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if root is None:
            return node
        ptr = root
        while True:
            if ptr.val>val:
                if ptr.left is None:
                    ptr.left = node
                    break
                ptr = ptr.left
            else:
                if ptr.right is None:
                    ptr.right = node
                    break
                ptr = ptr.right
        return root
