class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        q = deque()
        ans = -1
        def increment(s):
            return str((int(s)+1)%10)
        def decrement(s):
            if s=="0":
                return "9"
            return str(int(s)-1)
        
        visited = set()
        def bfs(combinations, depth):
            nonlocal ans
            if ans != -1:
                return
            if combinations in deadends: #todo: check better way to skip this(maybe trie)
                return
            if combinations in visited:
                return
            if combinations==target:
                ans = depth
                return
            visited.add(combinations)
            q.append((increment(combinations[0])+combinations[1]+combinations[2]+combinations[3], depth+1))
            q.append((decrement(combinations[0])+combinations[1]+combinations[2]+combinations[3], depth+1))
            q.append((combinations[0]+increment(combinations[1])+combinations[2]+combinations[3], depth+1))
            q.append((combinations[0]+decrement(combinations[1])+combinations[2]+combinations[3], depth+1))
            q.append((combinations[0]+combinations[1]+increment(combinations[2])+combinations[3], depth+1))
            q.append((combinations[0]+combinations[1]+decrement(combinations[2])+combinations[3], depth+1))
            q.append((combinations[0]+combinations[1]+combinations[2]+increment(combinations[3]), depth+1))
            q.append((combinations[0]+combinations[1]+combinations[2]+decrement(combinations[3]), depth+1))     
        q.append(("0000", 0))
        while len(q)>0:
            n = q.popleft()
            bfs(n[0], n[1])
        return ans