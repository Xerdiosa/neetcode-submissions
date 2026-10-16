class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):               
                if self._recurse(board,x,y,visited,0,word):
                    return True
        return False
    def _recurse(self, board, x, y, visited, idx, word) -> bool:
        if idx == len(word):
            return True
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
            return False
        if visited[x][y]:
            return False
        if board[x][y] != word[idx]:
            return False
        visited[x][y] = True
        res = self._recurse(board,x+1,y,visited,idx+1,word) or self._recurse(board,x-1,y,visited,idx+1,word) or self._recurse(board,x,y+1,visited,idx+1,word) or self._recurse(board,x,y-1,visited,idx+1,word)
        visited[x][y] = False
        return res