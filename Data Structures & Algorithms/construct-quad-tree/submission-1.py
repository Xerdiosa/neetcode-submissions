"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x,y,r):
            if r==1:
                return Node(val=True if grid[x][y]==1 else False, isLeaf=True)
            root = Node()
            root.topLeft = helper(x,y,r//2)
            root.topRight = helper(x,y+r//2,r//2)
            root.bottomLeft = helper(x+r//2,y,r//2)
            root.bottomRight = helper(x+r//2,y+r//2,r//2)
            if root.topLeft.isLeaf and root.topRight.isLeaf and root.bottomLeft.isLeaf and root.bottomRight.isLeaf and root.topLeft.val==root.topRight.val and root.topRight.val==root.bottomLeft.val and root.bottomLeft.val==root.bottomRight.val:
                root.isLeaf=True
                root.val=root.topLeft.val
                root.topLeft=None
                root.topRight=None
                root.bottomLeft=None
                root.bottomRight=None
            return root
        return helper(0,0,len(grid))
