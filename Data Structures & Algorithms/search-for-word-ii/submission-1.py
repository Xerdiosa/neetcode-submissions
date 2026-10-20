class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = dict()
        matched = set()
        ans = []
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for word in words:
            ptr = trie
            for letter in list(word):
                if letter not in ptr:
                    ptr[letter] = dict()
                ptr=ptr[letter]
            ptr["_end_"] = word
        def helper(x,y,ptr):
            if "_end_" in ptr and ptr["_end_"] not in matched:
                ans.append(ptr["_end_"])
                matched.add(ptr["_end_"])
            if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                return
            if visited[x][y]:
                return
            if board[x][y] in ptr:
                visited[x][y] = True
                helper(x+1,y,ptr[board[x][y]])
                helper(x-1,y,ptr[board[x][y]])
                helper(x,y+1,ptr[board[x][y]])
                helper(x,y-1,ptr[board[x][y]])
                visited[x][y] = False
        for x in range(len(board)):
            for y in range(len(board[0])):
                helper(x,y,trie)
        return ans
        


        