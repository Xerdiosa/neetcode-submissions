"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = dict()
        def helper(n: Optional['Node']) -> Optional['Node']:
            if n is None:
                return None
            if n.val in visited:
                return visited[n.val]
            visited[n.val] = Node(val=n.val, neighbors = None)
            if len(n.neighbors) > 0:
                visited[n.val].neighbors = []
                for i in n.neighbors:
                    visited[n.val].neighbors.append(helper(i))
            return visited[n.val]
        return helper(node)

        def helper(n: Optional['Node']) -> Optional['Node']:
            if n is None:
                return None
            if n.val in visited:
                return visited[n.val]
            visited[n.val] = Node(val=n.val, neighbors = None)
            if len(n.neighbors) > 0:
                visited[n.val].neighbors = []
                for i in n.neighbors:
                    visited[n.val].neighbors.append(helper(i))
            return visited[n.val]