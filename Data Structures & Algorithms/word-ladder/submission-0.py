class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        allword=wordList[:]
        allword.append(beginWord)
        allword.append(endWord)
        def transformable(a,b):
            cnt=0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    cnt+=1
                if cnt>1:
                    return False
            return True
        paths = dict()
        for i in allword:
            paths[i]=[]
        for i in range(len(allword)):
            for j in range(i+1, len(allword)):
                if not transformable(allword[i], allword[j]):
                    continue
                paths[allword[i]].append(allword[j])
                paths[allword[j]].append(allword[i])
        from collections import deque
        q = deque()
        #append or popleft
        ans = 0
        visited = set()

        def helper(word, step):
            nonlocal ans
            if ans > 0:
                return
            if word in visited:
                return
            visited.add(word)
            if word==endWord:
                ans=step
                return
            for nextWord in paths[word]:
                q.append((nextWord,step+1))

        visited.add(beginWord)
        for word in paths[beginWord]:
            q.append((word,2))

        while len(q)>0:
            param = q.popleft()
            helper(param[0],param[1])
        return ans