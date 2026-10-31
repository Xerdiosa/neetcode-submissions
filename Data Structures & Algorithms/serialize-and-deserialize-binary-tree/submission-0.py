# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def helper(r):
            ans.append(str(r.left.val) if r.left is not None else "null")
            ans.append(str(r.right.val) if r.right is not None else "null")
            if r.left is not None:
                helper(r.left)
            if r.right is not None:
                helper(r.right)
        if root is None:
            ans.append("")
            return ",".join(ans)
        ans.append(str(root.val))
        helper(root)
        while ans[-1]=="null":
            ans.pop()
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        datas = data.split(",")
        idx = 0
        root = TreeNode(int(datas[0]))
        def helper(r):
            nonlocal idx
            if idx>=len(datas):
                return
            if idx+1<len(datas) and datas[idx+1]!="null":
                r.left = TreeNode(int(datas[idx+1]))
            if idx+2<len(datas) and datas[idx+2]!="null":
                r.right = TreeNode(int(datas[idx+2]))
            if r.left is not None:
                idx+=2
                helper(r.left)    
            if r.right is not None:
                idx+=2
                helper(r.right)
        helper(root)
        return root
